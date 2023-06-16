// import API from './API';
import axios from "axios"
import React, { useState, useContext } from 'react';
import { View, StyleSheet } from 'react-native';
import { Text, TextInput, Button } from 'react-native-paper';
import { CsrfTokenContext } from "./CsrfTokenContext";

const SignUpScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [verifyPassword, setVerifyPassword] = useState('');
  const [emailError, setEmailError] = useState(undefined);
  const [usernameError, setUsernameError] = useState(undefined);
  const [passwordError, setPasswordError] = useState(undefined);
  const [verifyPasswordError, setVerifyPasswordError] = useState(undefined);
  const csrfToken = useContext(CsrfTokenContext);

  const server_url = "http://192.168.1.119:8000/user/register/";

  const handleSignUp = async () => {
    const formData = new FormData();
    formData.append('email', email);
    formData.append('username', username);
    formData.append('password1', password);
    formData.append('password2', verifyPassword);


    await axios.post(server_url, formData, {
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        console.log(response.data);
        console.log('Sign up successful');
        navigation.navigate('PersonalInfo');
      })
      .catch((error) => {
        console.log("error: ", error.response.data.errors);
        const errors = JSON.parse(error.response.data.errors);
        if (errors.email == undefined)
          setEmailError(undefined);
        else
          setEmailError(errors.email[0].message);
        if (errors.username == undefined)
          setUsernameError(undefined);
        else
          setUsernameError(errors.username[0].message);
        if (errors.password1 == undefined)
          setPasswordError(undefined);
        else
          setPasswordError(errors.password1[0].message);
        if (errors.password2 == undefined)
          setVerifyPasswordError(undefined);
        else
          setVerifyPasswordError(errors.password2[0].message);
      }
      );
  };



  return (
    <View style={styles.container}>
      <TextInput
        label="Email"
        value={email}
        onChangeText={setEmail}
        style={styles.input}
        error={emailError}
      />
      {
        emailError && <Text style={{ color: 'red' }}>{emailError}</Text>
      }
      <TextInput
        label="Username"
        value={username}
        onChangeText={setUsername}
        style={styles.input}
        error={usernameError}
      />
      {
        usernameError && <Text style={{ color: 'red' }}>{usernameError}</Text>
      }
      <TextInput
        label="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
        style={styles.input}
        error={passwordError}
      />
      {
        passwordError && <Text style={{ color: 'red' }}>{passwordError}</Text>
      }
      <TextInput
        label="Verify Password"
        value={verifyPassword}
        onChangeText={setVerifyPassword}
        secureTextEntry
        style={styles.input}
        error={verifyPasswordError}
      />
      {
        verifyPasswordError && <Text style={{ color: 'red' }}>{verifyPasswordError}</Text>
      }


      <Button mode="contained" onPress={handleSignUp} style={styles.button}>
        Next
      </Button>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    justifyContent: 'center',
  },
  input: {
    marginBottom: 16,
  },
  button: {
    marginTop: 16,
  },
});

export default SignUpScreen;
