import React from 'react';
import { View, TouchableOpacity, StyleSheet, ImageBackground, Text } from 'react-native';

const Roomit = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <ImageBackground
        source={require('./assets/roomit_background_last.jpg')}
        style={styles.backgroundImage}
      >
        <View style={styles.contentContainer}>
          <View style={styles.buttonContainer}>
            <TouchableOpacity
              style={[styles.button, { backgroundColor: "#416788" }]}
              onPress={() => navigation.navigate('SignIn')}
            >
              <Text style={styles.buttonText}>SIGN IN</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[styles.button, { backgroundColor: "#D7D7C2" }]}
              onPress={() => navigation.navigate('SignUpScreen')}
            >
              <Text style={styles.buttonText}>SIGN UP</Text>
            </TouchableOpacity>
          </View>
        </View>
      </ImageBackground>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  backgroundImage: {
    flex: 1,
    resizeMode: 'cover',
    width: '100%',
    height: '100%',
  },
  contentContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 220,
  },
  buttonContainer: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  button: {
    width: 200,
    height: 50,
    padding: 10,
    borderRadius: 5,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 10,
  },
  buttonText: {
    fontSize: 21,
    color: '#FFFFFF',
  },
});

export default Roomit;
