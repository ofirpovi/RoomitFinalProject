// import React, { useState, useEffect } from 'react';
// import { View, StyleSheet, Button, Image } from 'react-native';
// import * as ImagePicker from 'expo-image-picker';

// const UploadPhotoComp = ({ onImageSelect }) => {
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
//       onImageSelect(result.uri);
//     }
//   };

//   if (!isFontLoaded) {
//     return null;
//   }

//   return (
//     <View style={styles.container}>
//       {selectedImage && <Image source={{ uri: selectedImage }} style={styles.image} />}
//       <Button title="Select Image" onPress={handleImageSelect} />
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

// export default UploadPhotoComp;


import React, { useState, useEffect } from 'react';
import { View, StyleSheet, Button, Image } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

const UploadPhotoComp = ({ onImageSelect }) => {
  const [isFontLoaded, setIsFontLoaded] = useState(false);

  useEffect(() => {
    const loadFonts = async () => {
      setIsFontLoaded(true);
    };

    loadFonts();
  }, []);

  const handleImageSelect = async () => {
    const permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync();

    if (permissionResult.granted === false) {
      alert('Permission to access the camera roll is required!');
      return;
    }

    const result = await ImagePicker.launchImageLibraryAsync();

    if (!result.cancelled) {
      onImageSelect(result.uri);
    }
  };

  if (!isFontLoaded) {
    return null;
  }

  return (
    <View style={styles.container}>
      <Button title="Select Image" onPress={handleImageSelect} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginRight: 8,
    marginBottom: 8,
  },
});

export default UploadPhotoComp;
