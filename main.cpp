#include <iostream>
#include <memory>
#include <algorithm>
#include <initializer_list>
#include <stdexcept>
#include <utility>
#include <iterator> // Include for std::begin and std::end

// Template class for a generic container
template<typename T>
class Container {
private:
    std::shared_ptr<T[]> data; // Smart pointer to dynamically allocated array
    size_t size;

public:
    // Constructors
    Container(size_t size) : size(size), data(new T[size]) {}

    // Constructor with initializer list
    Container(std::initializer_list<T> init) : size(init.size()), data(new T[init.size()]) {
        std::copy(init.begin(), init.end(), data.get());
    }

    // Copy constructor
    Container(const Container<T>& other) : size(other.size), data(new T[other.size]) {
        std::copy(other.data.get(), other.data.get() + size, data.get());
    }

    // Move constructor
    Container(Container<T>&& other) noexcept : size(std::exchange(other.size, 0)), data(std::move(other.data)) {}

    // Destructor
    ~Container() = default;

    // Assignment operator
    Container<T>& operator=(const Container<T>& other) {
        if (this != &other) {
            size = other.size;
            data.reset(new T[size]);
            std::copy(other.data.get(), other.data.get() + size, data.get());
        }
        return *this;
    }

    // Move assignment operator
    Container<T>& operator=(Container<T>&& other) noexcept {
        if (this != &other) {
            size = std::exchange(other.size, 0);
            data = std::move(other.data);
        }
        return *this;
    }

    // Method to access elements using subscript operator
    T& operator[](size_t index) {
        if (index >= size) {
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }

    // Method to access elements using const subscript operator
    const T& operator[](size_t index) const {
        if (index >= size) {
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }

    // Method to get size
    size_t getSize() const {
        return size;
    }

    // Iterator support
    using iterator = T*;
    using const_iterator = const T*;

    iterator begin() {
        return data.get();
    }

    iterator end() {
        return data.get() + size;
    }

    const_iterator begin() const {
        return data.get();
    }

    const_iterator end() const {
        return data.get() + size;
    }
};

int main() {
    // Create a Container of integers with size 5
    Container<int> intContainer(5);

    // Fill the container with values using initializer list
    Container<int> anotherContainer = {1, 2, 3, 4, 5};

    // Copy constructor demonstration
    Container<int> copiedContainer = anotherContainer;

    // Move constructor demonstration
    Container<int> movedContainer = std::move(anotherContainer);

    // Print the container values using range-based for loop
    for (const auto& item : intContainer) {
        std::cout << item << " ";
    }
    std::cout << std::endl;

    return 0;
}
