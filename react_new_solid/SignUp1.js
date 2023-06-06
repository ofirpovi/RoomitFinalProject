import React from 'react';
import { View, Text, Button } from 'react-native';
import { useNavigation } from '@react-navigation/native';

function SignUp1() {
  const navigation = useNavigation();

  function handlePress1() {
    navigation.navigate('Screen1');
  }

  function handlePress3() {
    navigation.navigate('Screen3');
  }

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Welcome to Screen 2</Text>
      <Button title="Go to Screen 1" onPress={handlePress1} />
      <Button title="Go to Screen 3" onPress={handlePress3} />
    </View>
  );
}

export default SignUp1;
