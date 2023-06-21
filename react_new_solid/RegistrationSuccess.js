import React from 'react';
import { View, StyleSheet, Text, Button } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import axios from "axios";

const RegistrationSuccess = ({ navigation, route }) => {
  console.log("RegistrationSuccess");
  console.log(route.params.username);
  const username = route.params.username;

  const handleGoBack = () => {
    navigation.navigate('MainPage_ForARoomate', {username: username});
  };

  return (
    <View style={styles.container}>
      <Text style={styles.message}>Registration Successful!</Text>
      <Button title="Go back to the home page" onPress={handleGoBack} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  message: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 20,
  },
});

export default RegistrationSuccess;
