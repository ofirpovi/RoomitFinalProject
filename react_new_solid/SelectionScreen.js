import React, { useState } from 'react';
import { View, StyleSheet, Text } from 'react-native';
import { Button } from 'react-native-paper';

const SelectionScreen = ({ navigation, route }) => {
  console.log("SelectionScreen");
  console.log(route.params.username);
  const [selectedOption, setSelectedOption] = useState('');
  const username = route.params.username;

  const handleOptionSelect = (option) => {
    setSelectedOption(option);
  };

  const handleSubmit = () => {
    if (selectedOption === 'Looking for a Roommate') {
      console.log("SuccessRoommateFromSelection");
      navigation.navigate('SuccessRoommate', {username: username});
    } else if (selectedOption === 'Looking for a Property') {
      navigation.navigate('SuccessProperty', {username: username});
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.buttonContainer}>
        <Button
          mode="contained"
          onPress={() => handleOptionSelect('Looking for a Roommate')}
          style={[styles.button, selectedOption === 'Looking for a Roommate' && styles.selectedButton]}
          contentStyle={styles.buttonContent}
          labelStyle={styles.buttonLabel}
        >
          <View>
            <Text style={styles.buttonSubText}>Looking for a</Text>
            <Text style={styles.buttonText}>Roommate</Text>
          </View>
        </Button>
        <Button
          mode="contained"
          onPress={() => handleOptionSelect('Looking for a Property')}
          style={[styles.button, selectedOption === 'Looking for a Property' && styles.selectedButton]}
          contentStyle={styles.buttonContent}
          labelStyle={styles.buttonLabel}
        >
          <View>
            <Text style={styles.buttonSubText}>Looking for a</Text>
            <Text style={styles.buttonText}>Property</Text>
          </View>
        </Button>
      </View>
      <Button mode="contained" onPress={handleSubmit} style={styles.submitButton}>
        Submit
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    justifyContent: 'center',
  },
  buttonContainer: {
    flexDirection: 'row',
    marginBottom: 16,
  },
  button: {
    flex: 1,
    marginRight: 8,
    borderRadius: 0, // Remove button border radius
    height: 80, // Increase the height of the button
  },
  selectedButton: {
    backgroundColor: '#00c853', // Example color for selected button
  },
  buttonContent: {
    width: '100%',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonLabel: {
    textAlign: 'center', // Center the button label
  },
  buttonText: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  buttonSubText: {
    fontSize: 16,
    textAlign: 'center',
  },
  submitButton: {
    marginTop: 16,
  },
});

export default SelectionScreen;
