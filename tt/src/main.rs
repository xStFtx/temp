extern crate rand;

use rand::distributions::{Distribution, Uniform};
use rand::Rng;
use std::fs::File;
use std::io::{BufRead, BufReader};

// Define a simple Neural Network structure
struct NeuralNetwork {
    input_size: usize,
    hidden_layers: Vec<HiddenLayer>,
    output_size: usize,
    training_iterations: usize,
    learning_rate: f64,
    momentum: f64,
    weight_decay: f64,
}

struct HiddenLayer {
    size: usize,
    weights: Vec<Vec<f64>>,
    biases: Vec<f64>,
    activations: Vec<f64>,
    activation_fn: fn(f64) -> f64,
    activation_fn_prime: fn(f64) -> f64,
}

impl NeuralNetwork {
    // Constructor with Xavier/Glorot initialization
    fn new(
        input_size: usize,
        hidden_layers: Vec<(usize, fn(f64) -> f64, fn(f64) -> f64)>,
        output_size: usize,
        learning_rate: f64,
        momentum: f64,
        weight_decay: f64,
    ) -> Self {
        let mut rng = rand::thread_rng();
        let mut xavier_init = |input: usize, output: usize| {
            let limit = (6.0 / (input + output) as f64).sqrt();
            let uniform = Uniform::new(-limit, limit);
            (0..output).map(|_| uniform.sample(&mut rng)).collect()
        };

        let hidden_layers: Vec<HiddenLayer> = hidden_layers
            .into_iter()
            .map(|(size, activation_fn, activation_fn_prime)| {
                let weights: Vec<f64> = xavier_init(input_size, size);
                let biases: Vec<f64> = (0..size).map(|_| rng.gen_range(-1.0..1.0)).collect();

                HiddenLayer {
                    size,
                    weights: vec![weights.clone(); size],
                    biases,
                    activations: vec![0.0; size],
                    activation_fn,
                    activation_fn_prime,
                }
            })
            .collect();

        NeuralNetwork {
            input_size,
            hidden_layers,
            output_size,
            training_iterations: 0,
            learning_rate,
            momentum,
            weight_decay,
        }
    }

    // Forward propagation
    fn predict(&mut self, input: &[f64]) -> Vec<f64> {
        let mut activations = input.to_vec();

        for layer in &mut self.hidden_layers {
            activations = layer.forward(&activations);
        }

        let output_weights: Vec<f64> = self
            .hidden_layers
            .last()
            .expect("At least one hidden layer required")
            .activations
            .iter()
            .enumerate()
            .map(|(i, &activation)| {
                (0..self.output_size)
                    .map(|j| self.hidden_layers.last().unwrap().weights[j][i] * activation)
                    .sum::<f64>()
            })
            .collect();

        output_weights
    }

    // Backpropagation and weight update
    fn train(&mut self, input: &[f64], target: &[f64]) {
        // Forward propagation
        let output = self.predict(input);

        // Compute output layer error
        let output_errors: Vec<f64> = output
            .iter()
            .zip(target)
            .map(|(o, t)| t - o)
            .collect();

        // Backpropagate errors through the network
        let mut hidden_errors = output_errors.clone();
        for layer in self.hidden_layers.iter_mut().rev() {
            hidden_errors = layer.backward(&hidden_errors);
        }

        // Update weights and biases with momentum and weight decay
        for i in 0..self.hidden_layers.len() {
            if i == 0 {
                self.hidden_layers[i].update_weights(&input.to_vec(), &hidden_errors, self.learning_rate, self.momentum, self.weight_decay);
            } else {
                self.hidden_layers[i].update_weights(
                    &self.hidden_layers[i - 1].activations.clone(),
                    &hidden_errors,
                    self.learning_rate,
                    self.momentum,
                    self.weight_decay,
                );
            }
        }

        self.training_iterations += 1;
    }

    // Advanced training method with mini-batch support
    fn train_mini_batch(&mut self, inputs: &[Vec<f64>], targets: &[Vec<f64>]) {
        let batch_size = inputs.len();

        // Compute gradients for each mini-batch
        let mut output_errors: Vec<Vec<f64>> = Vec::with_capacity(batch_size);
        let mut hidden_errors: Vec<Vec<Vec<f64>>> =
            vec![vec![vec![0.0; self.hidden_layers[0].size]; batch_size]; self.hidden_layers.len()];

        for (input, target) in inputs.iter().zip(targets) {
            let output = self.predict(input);
            output_errors.push(
                output
                    .iter()
                    .zip(target)
                    .map(|(o, t)| t - o)
                    .collect(),
            );

            let mut layer_errors = output_errors.last().unwrap().clone();
            for i in 0..self.hidden_layers.len() {
                hidden_errors[i].extend(self.hidden_layers[i].backward(&layer_errors).into_iter().map(|e| vec![e; batch_size]));
                layer_errors = hidden_errors[i].iter().map(|v| v.iter().sum::<f64>() / batch_size as f64).collect();
            }
        }

        // Update weights and biases with momentum and weight decay
        for i in 0..self.hidden_layers.len() {
            if i == 0 {
                self.hidden_layers[i].update_weights_batch(
                    &inputs.to_vec(),
                    &hidden_errors[i],
                    self.learning_rate,
                    self.momentum,
                    self.weight_decay,
                );
            } else {
                self.hidden_layers[i].update_weights_batch(
                    &self.hidden_layers[i - 1]
                        .activations
                        .chunks(self.hidden_layers[i - 1].size)
                        .map(|chunk| chunk.to_vec())
                        .collect::<Vec<_>>(),
                    &hidden_errors[i],
                    self.learning_rate,
                    self.momentum,
                    self.weight_decay,
                );
            }
        }

        self.training_iterations += 1;
    }

    fn load_data(filename: &str) -> (Vec<Vec<f64>>, Vec<Vec<f64>>) {
        let file = File::open(filename).expect("Failed to open file");
        let reader = BufReader::new(file);

        let mut inputs: Vec<Vec<f64>> = Vec::new();
        let mut targets: Vec<Vec<f64>> = Vec::new();

        for line in reader.lines() {
            let line = line.expect("Failed to read line");
            let values: Vec<f64> = line
                .split(',')
                .map(|s| s.trim().parse().expect("Failed to parse value"))
                .collect();

            let input = values[..values.len() - 1].to_vec();
            let target = vec![values[values.len() - 1]];

            inputs.push(input);
            targets.push(target);
        }

        (inputs, targets)
    }

    fn save_model(&self, _filename: &str) {
        // Implementation to save model weights and architecture
    }

    fn load_model(&mut self, _filename: &str) {
        // Implementation to load model weights and architecture
    }
}

impl HiddenLayer {
    fn forward(&mut self, input: &[f64]) -> Vec<f64> {
        self.activations = input
            .iter()
            .enumerate()
            .map(|(i, &v)| {
                let activation = self.weights.iter().zip(input).map(|(w, x)| w[i] * x).sum::<f64>() + self.biases[i];
                (self.activation_fn)(activation)
            })
            .collect();

        self.activations.clone()
    }

    fn backward(&self, output_errors: &[f64]) -> Vec<f64> {
        output_errors
            .iter()
            .enumerate()
            .map(|(i, &error)| {
                let activation_prime = (self.activation_fn_prime)(self.activations[i]);
                error * activation_prime
            })
            .collect()
    }

    fn update_weights(
        &mut self,
        input: &[f64],
        errors: &[f64],
        learning_rate: f64,
        momentum: f64,
        weight_decay: f64,
    ) {
        for (i, weight) in self.weights.iter_mut().enumerate() {
            for (j, w) in weight.iter_mut().enumerate() {
                let delta = errors[i] * input[j];
                *w = *w * (1.0 - learning_rate * weight_decay) - learning_rate * delta + momentum * *w;
            }
        }

        for (i, bias) in self.biases.iter_mut().enumerate() {
            *bias = *bias - learning_rate * errors[i];
        }
    }

    fn update_weights_batch(
        &mut self,
        inputs: &[Vec<f64>],
        errors: &[Vec<f64>],
        learning_rate: f64,
        momentum: f64,
        weight_decay: f64,
    ) {
        let batch_size = inputs.len();

        for (i, weight) in self.weights.iter_mut().enumerate() {
            for (j, w) in weight.iter_mut().enumerate() {
                let delta = inputs.iter().zip(errors).map(|(input, error)| error[i] * input[j]).sum::<f64>() / batch_size as f64;
                *w = *w * (1.0 - learning_rate * weight_decay) - learning_rate * delta + momentum * *w;
            }
        }

        for (i, bias) in self.biases.iter_mut().enumerate() {
            *bias = *bias - learning_rate * errors.iter().map(|error| error[i]).sum::<f64>() / batch_size as f64;
        }
    }
}

// Declare the activation functions and their derivatives
fn sigmoid(x: f64) -> f64 {
    1.0 / (1.0 + (-x).exp())
}

fn sigmoid_derivative(x: f64) -> f64 {
    let sig = sigmoid(x);
    sig * (1.0 - sig)
}

fn relu(x: f64) -> f64 {
    x.max(0.0)
}

fn relu_derivative(x: f64) -> f64 {
    if x > 0.0 { 1.0 } else { 0.0 }
}

fn main() {
    // Example usage of the NeuralNetwork
    let input_size = 2;
    let hidden_layers = vec![
        (3 as usize, sigmoid as fn(f64) -> f64, sigmoid_derivative as fn(f64) -> f64),
    ];
    let output_size = 1;
    let learning_rate = 0.1;
    let momentum = 0.9;
    let weight_decay = 0.0001;

    // Create a tuple with function types (without calling the functions)
    let hidden_layer_config =
        (3 as usize, sigmoid as fn(f64) -> f64, sigmoid_derivative as fn(f64) -> f64);

    let mut nn = NeuralNetwork::new(
        input_size,
        vec![hidden_layer_config],
        output_size,
        learning_rate,
        momentum,
        weight_decay,
    );

    // Load training data from a file
    let (inputs, targets) = NeuralNetwork::load_data("data.csv");

    // Training the network with mini-batches
    let batch_size = 100;
    for epoch in 0..10 {
        let batches: Vec<_> = inputs.chunks(batch_size).zip(targets.chunks(batch_size)).collect();
        for (batch_inputs, batch_targets) in batches {
            nn.train_mini_batch(batch_inputs, batch_targets);
        }
    }

    // Testing the network after training
    let prediction = nn.predict(&inputs[0]);

    println!("Input: {:?}", inputs[0]);
    println!("Target: {:?}", targets[0]);
    println!("Prediction: {:?}", prediction);
    println!("Training Iterations: {}", nn.training_iterations);

    // Save and load the model
    nn.save_model("model.dat");
    nn.load_model("model.dat");
}
