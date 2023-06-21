// import React from 'react';
// import { View, Text, Button } from 'react-native';
// import { useNavigation } from '@react-navigation/native';

// function SignIn() {
//   const navigation = useNavigation();

//   <Text>Sign In Page</Text>

//   function handlePress1() {
//     navigation.navigate('Screen1');
//   }

//   function handlePress3() {
//     navigation.navigate('Screen3');
//   }

//   return (
//     <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
//       <Text>Sign In</Text>
//       <Button title="Go to Screen 1" onPress={handlePress1} />
//       <Button title="Go to Screen 3" onPress={handlePress3} />
//     </View>
//   );
// }

// export default SignIn;
//bla

import React, { useState } from 'react';
import { View, TextInput, Button, Text, Alert, StyleSheet, TouchableOpacity } from 'react-native';

const SignIn = ({ navigation }) => {
  const [inputTextEmail, setInputTextEmail] = useState('');
  const [inputTextPassword, setInputTextPassword] = useState('');
  const [savedText, setSavedText] = useState('');

  const handleInputChangeEmail = (text) => {
    setInputTextEmail(text);
    //setInputTextPassword(text);
  };

  const handleInputChangePassword = (text) => {
    setInputTextPassword(text);
    //setInputTextPassword(text);
  };


  const handleForgotPassword = () => {
    // Save the inputText variable to a database or do something else with it
    Alert.alert('Dont Worry!', 'we will sent your email the password.', [
      {
        text: 'OK',
        onPress: () => console.log('OK Pressed')
      }
    ]);
  };

  const handleSave = () => {
    // Save the inputText variable to a database or do something else with it
    setSavedText();
    Alert.alert('You are logged in!', 'Your input has been saved.', [
      {
        text: 'OK',
        onPress: () => console.log('OK Pressed')
      }
    ]);
  };

  const ForgotPasswordButton = ({ onPress }) => (
    <TouchableOpacity style={styles.forgotPasswordButton} onPress={onPress}>
      <Text style={styles.forgotPasswordButtonText}>Forgot your password?</Text>
    </TouchableOpacity>
  );


  const LogInButton = ({ onPress }) => (
    <TouchableOpacity style={styles.logInButton} onPress={onPress}>
      <Text style={styles.logInButtonText}>LOG IN</Text>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>

      <Text style={styles.title}>Roomit</Text>  

      <View style={styles.container2}>

      <Text style={{ fontSize: 16, marginBottom: 10 }}>Username:</Text>
    <TextInput style={{ fontSize: 12, marginBottom: 50 }}
      placeholder="Enter your username"
      onChangeText={handleInputChangeEmail}
      value={inputTextEmail}
    />
     <Text style={{ fontSize: 16, marginBottom: 10 }}>Password:</Text>
     <TextInput style={{ fontSize: 12, marginBottom: 120 }}
      placeholder="Enter your password"
      onChangeText={handleInputChangePassword}
      value={inputTextPassword}
      secureTextEntry={true}
    />
    <TouchableOpacity style={styles.logInButton} onPress={() => navigation.navigate('MainPage_ForARoomate', {username: inputTextEmail})}>
        <Text style={styles.logInButtonText}>LOG IN</Text>
    </TouchableOpacity>
    <ForgotPasswordButton onPress={handleForgotPassword} />

    </View>
  </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    textAlign: 'center',
    alignItems: 'center',
    backgroundColor: '#EEF9F5',
  },
  title: {
    fontSize: 25,
    fontWeight: 'bold',
    color: '#499262',
    fontFamily: 'Courgette-Regular',
    paddingVertical: 0,
    textAlign: 'center',
    alignItems: 'center',
  },
  container2: {
    flex: 1,
    paddingTop: 180,
    textAlign: 'center',
    alignItems: 'center',
    backgroundColor: '#EEF9F5',
  },
  logInButton: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 5,
    marginBottom: 20,
  },
  logInButtonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  forgotPasswordButton: {
    paddingVertical: 10,
    paddingHorizontal: 20,
    marginVertical: 10,
    borderRadius: 5,
  },
  forgotPasswordButtonText: {
    color: '#838383',
    fontSize: 14,
  },
});

export default SignIn;