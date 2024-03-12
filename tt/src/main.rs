extern crate rand;

use rand::Rng;

// Define a simple Neural Network structure
struct NeuralNetwork {
    input_size: usize,
    hidden_size: usize,
    output_size: usize,
    weights_ih: Vec<Vec<f64>>,
    weights_ho: Vec<Vec<f64>>,
    bias_h: Vec<f64>,
    bias_o: Vec<f64>,
}

impl NeuralNetwork {
    // Constructor to initialize the neural network
    fn new(input_size: usize, hidden_size: usize, output_size: usize) -> Self {
        let mut rng = rand::thread_rng();

        let weights_ih: Vec<Vec<f64>> = (0..hidden_size)
            .map(|_| (0..input_size).map(|_| rng.gen_range(-1.0..1.0)).collect())
            .collect();

        let weights_ho: Vec<Vec<f64>> = (0..output_size)
            .map(|_| (0..hidden_size).map(|_| rng.gen_range(-1.0..1.0)).collect())
            .collect();

        let bias_h: Vec<f64> = (0..hidden_size).map(|_| rng.gen_range(-1.0..1.0)).collect();
        let bias_o: Vec<f64> = (0..output_size).map(|_| rng.gen_range(-1.0..1.0)).collect();

        NeuralNetwork {
            input_size,
            hidden_size,
            output_size,
            weights_ih,
            weights_ho,
            bias_h,
            bias_o,
        }
    }

    // Sigmoid activation function
    fn sigmoid(x: f64) -> f64 {
        1.0 / (1.0 + (-x).exp())
    }

    // Derivative of the sigmoid function
    fn sigmoid_derivative(x: f64) -> f64 {
        let sig = NeuralNetwork::sigmoid(x);
        sig * (1.0 - sig)
    }

    // Mean Squared Error loss function
    fn mean_squared_error(expected: &[f64], actual: &[f64]) -> f64 {
        expected
            .iter()
            .zip(actual)
            .map(|(e, a)| (e - a).powi(2))
            .sum::<f64>()
            / expected.len() as f64
    }

    // Forward propagation
    fn predict(&self, input: &[f64]) -> Vec<f64> {
        let hidden: Vec<f64> = self
            .weights_ih
            .iter()
            .zip(&self.bias_h)
            .map(|(weights, bias)| {
                NeuralNetwork::sigmoid(
                    weights.iter().zip(input).map(|(w, i)| w * i).sum::<f64>() + bias,
                )
            })
            .collect();

        self.weights_ho
            .iter()
            .zip(&self.bias_o)
            .map(|(weights, bias)| {
                NeuralNetwork::sigmoid(
                    weights.iter().zip(&hidden).map(|(w, h)| w * h).sum::<f64>() + bias,
                )
            })
            .collect()
    }

    // Backpropagation and weight update
    fn train(&mut self, input: &[f64], target: &[f64], learning_rate: f64) {
        // Forward propagation
        let mut hidden: Vec<f64> = self
            .weights_ih
            .iter()
            .zip(&self.bias_h)
            .map(|(weights, bias)| {
                NeuralNetwork::sigmoid(
                    weights.iter().zip(input).map(|(w, i)| w * i).sum::<f64>() + bias,
                )
            })
            .collect();

        let output: Vec<f64> = self
            .weights_ho
            .iter()
            .zip(&self.bias_o)
            .map(|(weights, bias)| {
                NeuralNetwork::sigmoid(
                    weights.iter().zip(&hidden).map(|(w, h)| w * h).sum::<f64>() + bias,
                )
            })
            .collect();

        // Backpropagation
        let output_errors: Vec<f64> = target
            .iter()
            .zip(&output)
            .map(|(t, o)| NeuralNetwork::sigmoid_derivative(*o) * (t - o))
            .collect();

        let hidden_errors: Vec<f64> = self
            .weights_ho
            .iter()
            .flat_map(|weights| {
                weights.iter().zip(&output_errors).map(|(w, oe)| w * oe)
            })
            .collect();

        // Update weights and biases
        for (w, oe) in self.weights_ho.iter_mut().zip(&output_errors) {
            for (weight, h) in w.iter_mut().zip(&hidden) {
                *weight += learning_rate * oe * NeuralNetwork::sigmoid_derivative(*h);
            }
        }

        for (w, he) in self.weights_ih.iter_mut().zip(&hidden_errors) {
            for (weight, i) in w.iter_mut().zip(input) {
                *weight += learning_rate * he * NeuralNetwork::sigmoid_derivative(*i);
            }
        }

        // Update biases
        for (bias, oe) in self.bias_o.iter_mut().zip(&output_errors) {
            *bias += learning_rate * oe;
        }

        for (bias, he) in self.bias_h.iter_mut().zip(&hidden_errors) {
            *bias += learning_rate * he;
        }
    }
}

fn main() {
    // Example usage of the NeuralNetwork
    let input_size = 2;
    let hidden_size = 3;
    let output_size = 1;

    let mut nn = NeuralNetwork::new(input_size, hidden_size, output_size);

    let input_data = vec![0.5, 0.3];
    let target = vec![0.7];

    // Training the network
    for _ in 0..10000 {
        nn.train(&input_data, &target, 0.1);
    }

    // Testing the network after training
    let prediction = nn.predict(&input_data);

    println!("Input: {:?}", input_data);
    println!("Target: {:?}", target);
    println!("Prediction: {:?}", prediction);
    println!(
        "Mean Squared Error: {:.6}",
        NeuralNetwork::mean_squared_error(&target, &prediction)
    );
}
