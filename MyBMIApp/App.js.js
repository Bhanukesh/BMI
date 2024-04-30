import React, { useState } from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity } from 'react-native';

const App = () => {
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [bmi, setBmi] = useState(null);
  const [status, setStatus] = useState('');

  const calculateBMI = () => {
    const heightInMeters = height / 100; // Convert cm to meters
    const bmiValue = weight / (heightInMeters * heightInMeters);
    setBmi(bmiValue.toFixed(2)); // Format to 2 decimal places

    // Determine the health status based on BMI value
    if (bmiValue < 18.5) {
      setStatus('Underweight');
    } else if (bmiValue < 25) {
      setStatus('Normal weight');
    } else if (bmiValue < 30) {
      setStatus('Overweight');
    } else {
      setStatus('Obese');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to My BMI App</Text>
      <TextInput
        value={weight}
        onChangeText={setWeight}
        placeholder="Enter your weight (kg)"
        keyboardType="numeric"
        style={styles.input}
      />
      <TextInput
        value={height}
        onChangeText={setHeight}
        placeholder="Enter your height (cm)"
        keyboardType="numeric"
        style={styles.input}
      />
      <TouchableOpacity style={styles.button} onPress={calculateBMI}>
        <Text style={styles.buttonText}>Calculate BMI</Text>
      </TouchableOpacity>
      {bmi && (
        <View style={styles.result}>
          <Text style={styles.bmiText}>Your BMI is: {bmi}</Text>
          <Text style={styles.statusText}>Status: {status}</Text>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 24,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 24,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 12,
    borderRadius: 5,
    marginBottom: 16,
  },
  button: {
    backgroundColor: '#007bff',
    padding: 12,
    borderRadius: 5,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
  },
  result: {
    marginTop: 24,
    alignItems: 'center',
  },
  bmiText: {
    fontSize: 22,
    fontWeight: 'bold',
  },
  statusText: {
    fontSize: 20,
    marginTop: 8,
  },
});

export default App;
