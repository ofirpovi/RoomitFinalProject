import React from 'react';
import { View, Button } from 'react-native';

const NextButton = ({ onPress, disabled }) => {
  return (
    <View>
      <Button title="Next" onPress={onPress} disabled={disabled} />
    </View>
  );
};

export default NextButton;


