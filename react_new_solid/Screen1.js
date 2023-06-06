import React from 'react';
import { View, Text, Button, StyleSheet, ImageBackground, Image } from 'react-native';
import * as Font from 'expo-font';


const Screen1 = ({ navigation }) => {
  return (
    <View style={styles.container}>

      

      <ImageBackground 
        source={require('./assets/roomit_background2.png')}
        style={styles.backgroundImage}
      >

        <Text style={styles.title}>Roomit</Text>
        <Button
        title="SIGN IN"
        onPress={() => navigation.navigate('SignIn')}
        color="#409900"
      />
      <Button
        title="SIGN UP"
        onPress={() => navigation.navigate('SignUpScreen')}
        color="#000999"
      />
      </ImageBackground>

      
    </View>
  );
};

const styles = StyleSheet.create({
    container: {
      flex: 1,
      paddingTop: 0,
      textAlign: 'center',
      alignItems: 'center',
    },
    backgroundImage: {
      flex: 1,
      resizeMode: 'cover',
      width: '100%',
      height: '100%',
    },
    title: {
      fontSize: 70,
      fontWeight: 'bold',
      color: '#499262',
      fontFamily: 'Courgette-Regular',
      paddingVertical: 50,
      paddingTop: 100,
      textAlign: 'center',
      alignItems: 'center',
    },
    subtitle: {
      fontSize: 36,
      marginTop: 10
    },
  });

export default Screen1;
