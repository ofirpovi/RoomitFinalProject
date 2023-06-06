import React from 'react';
import { View, StyleSheet, Text, Button } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const RegistrationSuccess = () => {
  const navigation = useNavigation();

  const handleGoBack = () => {
    navigation.navigate('MainPage_ForARoomate');
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
