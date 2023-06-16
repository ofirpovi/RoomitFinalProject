import React, { useState } from 'react';
import { View, StyleSheet, Button, Image } from 'react-native';

const UploadPhoto = ({selectedImage, handleImageSelect}) => {
  return (
    <View style={styles.container}>
      <Image source={selectedImage} style={styles.image} />
      <Button title="Select Image" onPress={handleImageSelect} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  image: {
    width: 200,
    height: 200,
    marginBottom: 20,
  },
});

export default UploadPhoto;