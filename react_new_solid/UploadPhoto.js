// import React, { useState, useEffect } from 'react';
// import { View, StyleSheet, Button, Image } from 'react-native';
// import * as ImagePicker from 'expo-image-picker';

// const UploadPhoto = ({ navigation }) => {
//   const [selectedImage, setSelectedImage] = useState(null);
//   const [isFontLoaded, setIsFontLoaded] = useState(false);

//   useEffect(() => {
//     const loadFonts = async () => {
//       setIsFontLoaded(true);
//     };

//     loadFonts();
//   }, []);

//   const handleImageSelect = async () => {
//     const permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync();

//     if (permissionResult.granted === false) {
//       alert('Permission to access the camera roll is required!');
//       return;
//     }

//     const result = await ImagePicker.launchImageLibraryAsync();

//     if (!result.cancelled) {
//       setSelectedImage(result.uri);
//     }
//   };

//   const handleSubmit = () => {
//     console.log('Selected Image:', selectedImage);

//     navigation.navigate('AdditionalInfo');
//   };

//   if (!isFontLoaded) {
//     return null;
//   }

//   return (
//     <View style={styles.container}>
//       {selectedImage && <Image source={{ uri: selectedImage }} style={styles.image} />}
//       <Button title="Select Image" onPress={handleImageSelect} />
//       <Button title="Next" onPress={handleSubmit} disabled={!selectedImage} />
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: 'center',
//     alignItems: 'center',
//   },
//   image: {
//     width: 200,
//     height: 200,
//     marginBottom: 20,
//   },
// });

// export default UploadPhoto;





// UploadPhoto.js

import React, { useState } from 'react';
import { View, StyleSheet, Button, Image } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

const UploadPhoto = ({ navigation }) => {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageSelect = async () => {
    const permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync();

    if (permissionResult.granted === false) {
      alert('Permission to access the camera roll is required!');
      return;
    }

    const result = await ImagePicker.launchImageLibraryAsync();

    if (!result.cancelled) {
      setSelectedImage(result.uri);
    }
  };

  const handleSubmit = () => {
    console.log('Selected Image:', selectedImage);
    navigation.navigate('AdditionalInfo');
  };

  return (
    <View style={styles.container}>
      {selectedImage ? (
        <Image source={{ uri: selectedImage }} style={styles.image} />
      ) : (
        <Button title="Select Image" onPress={handleImageSelect} />
      )}
      {selectedImage && (
        <Button title="Next" onPress={handleSubmit} disabled={!selectedImage} />
      )}
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




// import React, { useState } from 'react';
// import { View, StyleSheet, Button, Image } from 'react-native';
// import * as ImagePicker from 'expo-image-picker';

// const UploadPhoto = ({ onImageSelect, onNext }) => {
//   const [selectedImage, setSelectedImage] = useState(null);

//   const handleImageSelect = async () => {
//     const permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync();

//     if (permissionResult.granted === false) {
//       alert('Permission to access the camera roll is required!');
//       return;
//     }

//     const result = await ImagePicker.launchImageLibraryAsync();

//     if (!result.cancelled) {
//       setSelectedImage(result.uri);
//       onImageSelect(result.uri);
//     }
//   };

//   return (
//     <View style={styles.container}>
//       {selectedImage && <Image source={{ uri: selectedImage }} style={styles.image} />}
//       <Button title="Select Image" onPress={handleImageSelect} />
//       <Button title="Next" onPress={onNext} disabled={!selectedImage} />
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: 'center',
//     alignItems: 'center',
//   },
//   image: {
//     width: 200,
//     height: 200,
//     marginBottom: 20,
//   },
// });

// export default UploadPhoto;
