// // import React from 'react';
// // import { View, Text, StyleSheet } from 'react-native';
// // import { Button } from 'react-native-paper';

// // // const SuccessRoommate = () => {
// // //   return (
// // //     <View style={styles.container}>
// // //       <Text style={styles.title}>Registration Successful!</Text>
// // //       <Text style={styles.subtitle}>Thank you for signing up.</Text>
// // //       <Text style={styles.info}>Please check your email for further instructions.</Text>
// // //       <Button mode="contained" style={styles.button}>
// // //         Continue
// // //       </Button>
// // //     </View>
// // //   );
// // // };

// // const SuccessRoommate = () => {
// //   return (
// //     <View style={styles.container}>
// //       <Text style={styles.title}>Enter your property details</Text>
// //       <Text style={styles.subtitle}>Thank you for signing up.</Text>
// //       <Text style={styles.info}>Please check your email for further instructions.</Text>
// //       <Button mode="contained" style={styles.button}>
// //         Continue
// //       </Button>
// //     </View>
// //   );
// // };


// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     padding: 16,
// //     justifyContent: 'center',
// //     alignItems: 'center',
// //   },
// //   title: {
// //     fontSize: 24,
// //     fontWeight: 'bold',
// //     marginBottom: 16,
// //     textAlign: 'center',
// //   },
// //   subtitle: {
// //     fontSize: 18,
// //     marginBottom: 16,
// //     textAlign: 'center',
// //   },
// //   info: {
// //     fontSize: 16,
// //     marginBottom: 24,
// //     textAlign: 'center',
// //   },
// //   button: {
// //     width: '50%',
// //     marginTop: 16,
// //   },
// // });

// // export default SuccessRoommate;



// // import React, { useState } from 'react';
// // import { View, StyleSheet, Text, TextInput, ScrollView, Image } from 'react-native';
// // import { Button } from 'react-native-paper';
// // import { Picker } from '@react-native-picker/picker';

// // const SuccessRoommate = () => {
// //   const [country, setCountry] = useState('');
// //   const [city, setCity] = useState('');
// //   const [neighborhood, setNeighborhood] = useState('');
// //   const [street, setStreet] = useState('');
// //   const [apartmentNumber, setApartmentNumber] = useState('');
// //   const [floorNumber, setFloorNumber] = useState('');
// //   const [description, setDescription] = useState('');
// //   const [rent, setRent] = useState('');
// //   const [rooms, setRooms] = useState('');
// //   const [photos, setPhotos] = useState([]);

// //   const handleAddPhoto = () => {
// //     // Implement logic to add a photo
// //     // ...
// //   };

// //   const handleRemovePhoto = (index) => {
// //     // Implement logic to remove a photo at the specified index
// //     // ...
// //   };

// //   const renderPhotos = () => {
// //     return photos.map((photo, index) => (
// //       <View key={index} style={styles.photoContainer}>
// //         <Image source={photo} style={styles.photo} />
// //         <Button onPress={() => handleRemovePhoto(index)}>Remove</Button>
// //       </View>
// //     ));
// //   };

// //   const handleSubmit = () => {
// //     // Implement logic to submit property details
// //     // ...
// //   };

// //   return (
// //     <ScrollView style={styles.container}>
// //       <Text style={styles.title}>Enter your property details please:</Text>

// //       <Text style={styles.label}>Country:</Text>
// //       <Picker selectedValue={country} onValueChange={(value) => setCountry(value)}>
// //         <Picker.Item label="Select country" value="" />
// //         {/* Add country options here */}
// //       </Picker>

// //       <Text style={styles.label}>City:</Text>
// //       <Picker selectedValue={city} onValueChange={(value) => setCity(value)}>
// //         <Picker.Item label="Select city" value="" />
// //         {/* Add city options here */}
// //       </Picker>

// //       <TextInput
// //         label="Neighborhood"
// //         value={neighborhood}
// //         onChangeText={setNeighborhood}
// //         style={styles.input}
// //       />

// //       <TextInput
// //         label="Street"
// //         value={street}
// //         onChangeText={setStreet}
// //         style={styles.input}
// //       />

// //       <TextInput
// //         label="Apartment Number (It will not be displayed)"
// //         value={apartmentNumber}
// //         onChangeText={setApartmentNumber}
// //         style={styles.input}
// //       />

// //       <TextInput
// //         label="Floor Number"
// //         value={floorNumber}
// //         onChangeText={setFloorNumber}
// //         style={styles.input}
// //       />

// //       <Text style={styles.label}>Description:</Text>
// //       <TextInput
// //         multiline
// //         numberOfLines={4}
// //         value={description}
// //         onChangeText={setDescription}
// //         style={styles.input}
// //       />

// //       <TextInput
// //         label="Rent"
// //         value={rent}
// //         onChangeText={setRent}
// //         style={styles.input}
// //         keyboardType="numeric"
// //       />

// //       <TextInput
// //         label="Rooms"
// //         value={rooms}
// //         onChangeText={setRooms}
// //         style={styles.input}
// //         keyboardType="numeric"
// //       />

// //       <Text style={styles.label}>Photos:</Text>
// //       <View style={styles.photosContainer}>
// //         {renderPhotos()}
// //         {photos.length < 8 && (
// //           <Button onPress={handleAddPhoto}>Add Photo</Button>
// //         )}
// //       </View>

// //       <Button mode="contained" onPress={handleSubmit} style={styles.submitButton}>
// //         Submit
// //       </Button>
// //     </ScrollView>
// //   );
// // };

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     padding: 16,
// //   },
// //   title: {
// //     fontSize: 18,
// //     fontWeight: 'bold',
// //     marginBottom: 16,
// //   },
// //   label: {
// //     fontSize: 16,
// //     fontWeight: 'bold',
// //     marginTop: 16,
// //   },
// //   input: {
// //     marginBottom: 16,
// //   },
// //   photosContainer: {
// //     flexDirection: 'row',
// //     flexWrap: 'wrap',
// //     marginBottom: 16,
// //   },
// //   photoContainer: {
// //     marginRight: 8,
// //     marginBottom: 8,
// //   },
// //   photo: {
// //     width: 80,
// //     height: 80,
// //     resizeMode: 'cover',
// //   },
// //   submitButton: {
// //     marginTop: 16,
// //   },
// // });

// // export default SuccessRoommate;




// // import React, { useState } from 'react';
// // import { View, StyleSheet, Text } from 'react-native';
// // import RNPickerSelect from 'react-native-picker-select';
// // import countries from 'countries-list'; // Import the countries package

// // const SuccessRoommate = () => {
// //   const [country, setCountry] = useState('');

// //   const handleCountryChange = (value) => {
// //     setCountry(value);
// //   };

// //   const handleSubmit = () => {
// //     // Perform necessary actions with the selected property details
// //     console.log('Property Details:', {
// //       country,
// //       // Include other property details
// //     });

// //     // Navigate to the next screen or perform other actions
// //     // ...
// //   };

// //   const countryOptions = Object.keys(countries.countries).map((countryCode) => {
// //     const countryName = countries.countries[countryCode].name;
// //     return { label: countryName, value: countryCode };
// //   });

// //   return (
// //     <View style={styles.container}>
// //       <Text style={styles.title}>Enter your property details, please:</Text>

// //       <Text style={styles.label}>Country:</Text>
// //       <RNPickerSelect
// //         onValueChange={handleCountryChange}
// //         value={country}
// //         placeholder={{ label: 'Select a country', value: null }}
// //         items={countryOptions}
// //         style={pickerSelectStyles}
// //       />

// //       {/* Add other property details inputs and components here */}

// //       <Button mode="contained" onPress={handleSubmit} style={styles.button}>
// //         Next
// //       </Button>
// //     </View>
// //   );
// // };

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     padding: 16,
// //     justifyContent: 'center',
// //   },
// //   title: {
// //     fontSize: 24,
// //     fontWeight: 'bold',
// //     marginBottom: 16,
// //   },
// //   label: {
// //     fontSize: 18,
// //     marginBottom: 8,
// //   },
// //   button: {
// //     marginTop: 16,
// //   },
// // });

// // const pickerSelectStyles = StyleSheet.create({
// //   inputIOS: {
// //     fontSize: 16,
// //     paddingVertical: 12,
// //     paddingHorizontal: 10,
// //     borderWidth: 1,
// //     borderColor: 'gray',
// //     borderRadius: 4,
// //     color: 'black',
// //     paddingRight: 30,
// //   },
// //   inputAndroid: {
// //     fontSize: 16,
// //     paddingHorizontal: 10,
// //     paddingVertical: 8,
// //     borderWidth: 0.5,
// //     borderColor: 'gray',
// //     borderRadius: 8,
// //     color: 'black',
// //     paddingRight: 30,
// //   },
// // });

// // export default SuccessRoommate;



// // import React, { useState } from 'react';
// // import { View, StyleSheet, Text } from 'react-native';
// // import RNPickerSelect from 'react-native-picker-select';

// // const SuccessRoommate = () => {
// //   const [country, setCountry] = useState('');

// //   const handleCountryChange = (value) => {
// //     setCountry(value);
// //   };

// //   const handleSubmit = () => {
// //     // Perform necessary actions with the selected property details
// //     console.log('Property Details:', {
// //       country,
// //       // Include other property details
// //     });

// //     // Navigate to the next screen or perform other actions
// //     // ...
// //   };

// //   const countryOptions = [
// //     { label: 'USA', value: 'USA' },
// //     { label: 'Canada', value: 'Canada' },
// //     { label: 'Australia', value: 'Australia' },
// //     // Add more country options as needed
// //   ];

// //   return (
// //     <View style={styles.container}>
// //       <Text style={styles.title}>Enter your property details, please:</Text>

// //       <Text style={styles.label}>Country:</Text>
// //       <RNPickerSelect
// //         onValueChange={handleCountryChange}
// //         value={country}
// //         placeholder={{ label: 'Select a country', value: null }}
// //         items={countryOptions}
// //         style={pickerSelectStyles}
// //       />

// //       {/* Add other property details inputs and components here */}

// //       <Button mode="contained" onPress={handleSubmit} style={styles.button}>
// //         Next
// //       </Button>
// //     </View>
// //   );
// // };

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     padding: 16,
// //     justifyContent: 'center',
// //   },
// //   title: {
// //     fontSize: 24,
// //     fontWeight: 'bold',
// //     marginBottom: 16,
// //   },
// //   label: {
// //     fontSize: 18,
// //     marginBottom: 8,
// //   },
// //   button: {
// //     marginTop: 16,
// //   },
// // });

// // const pickerSelectStyles = StyleSheet.create({
// //   inputIOS: {
// //     fontSize: 16,
// //     paddingVertical: 12,
// //     paddingHorizontal: 10,
// //     borderWidth: 1,
// //     borderColor: 'gray',
// //     borderRadius: 4,
// //     color: 'black',
// //     paddingRight: 30,
// //   },
// //   inputAndroid: {
// //     fontSize: 16,
// //     paddingHorizontal: 10,
// //     paddingVertical: 8,
// //     borderWidth: 0.5,
// //     borderColor: 'gray',
// //     borderRadius: 8,
// //     color: 'black',
// //     paddingRight: 30,
// //   },
// // });

// // export default SuccessRoommate;


// // import React, { useState, useRef } from 'react';
// // import { View, StyleSheet, Text, TextInput, ScrollView, Image, KeyboardAvoidingView } from 'react-native';
// // import { Button } from 'react-native-paper';
// // import { Picker } from '@react-native-picker/picker';

// // const SuccessRoommate = () => {
// //   const [country, setCountry] = useState('');
// //   const [city, setCity] = useState('');
// //   const [neighborhood, setNeighborhood] = useState('');
// //   const [street, setStreet] = useState('');
// //   const [apartmentNumber, setApartmentNumber] = useState('');
// //   const [floorNumber, setFloorNumber] = useState('');
// //   const [description, setDescription] = useState('');
// //   const [rent, setRent] = useState('');
// //   const [rooms, setRooms] = useState('');
// //   const [photos, setPhotos] = useState([]);

// //   const handleAddPhoto = () => {
// //     // Implement logic to add a photo
// //     // ...
// //   };

// //   const handleRemovePhoto = (index) => {
// //     // Implement logic to remove a photo at the specified index
// //     // ...
// //   };

// //   const renderPhotos = () => {
// //     return photos.map((photo, index) => (
// //       <View key={index} style={styles.photoContainer}>
// //         <Image source={photo} style={styles.photo} />
// //         <Button onPress={() => handleRemovePhoto(index)}>Remove</Button>
// //       </View>
// //     ));
// //   };

// //   const scrollViewRef = useRef();

// //   const handleSubmit = () => {
// //     // Implement logic to submit property details
// //     // ...

// //     // Scroll down a little after submitting
// //     scrollViewRef.current.scrollTo({ y: 400, animated: true });
// //   };

// //   return (
// //     <KeyboardAvoidingView style={styles.container} behavior="padding">
// //       <ScrollView ref={scrollViewRef}>
// //         <Text style={styles.title}>Enter your property details please:</Text>

// //         <View style={styles.inputContainer}>
// //           <Text style={styles.label}>Country:</Text>
// //           <Picker selectedValue={country} onValueChange={(value) => setCountry(value)}>
// //             <Picker.Item label="Select country" value="" />
// //             {/* Add country options here */}
// //           </Picker>
// //         </View>

// //         <View style={styles.inputContainer}>
// //           <Text style={styles.label}>City:</Text>
// //           <Picker selectedValue={city} onValueChange={(value) => setCity(value)}>
// //             <Picker.Item label="Select city" value="" />
// //             {/* Add city options here */}
// //           </Picker>
// //         </View>

// //         <View style={styles.inputContainer}>
// //           <Text style={styles.label}>Neighborhood:</Text>
// //           <TextInput
// //             value={neighborhood}
// //             onChangeText={setNeighborhood}
// //             style={styles.input}
// //           />
// //         </View>

// //         <View style={styles.inputContainer}>
// //           <Text style={styles.label}>Street:</Text>
// //           <TextInput
// //             value={street}
// //             onChangeText={setStreet}
// //             style={styles.input}
// //           />
// //         </View>

// //         <View style={styles.inputContainer}>
// //           <Text style={styles.label}>Apartment Number:</Text>
// //           <TextInput
// //             value={apartmentNumber}
// //             onChangeText={setApartmentNumber}
// //             style={styles.input}
// //           />
// //         </View>

// //         <View style={styles.inputContainer}>
// //           <Text style={styles.label}>Floor Number:</Text>
// //           <TextInput
// //             value={floorNumber}
// //             onChangeText={setFloorNumber}
// //             style={styles.input}
// //           />
// //         </View>

// //         <View style={styles.inputContainer}>
// //           <Text style={styles.label}>Description:</Text>
// //           <TextInput
// //             multiline
// //             numberOfLines={4}
// //             value={description}
// //             onChangeText={setDescription}
// //             style={styles.input}
// //           />
// //         </View>

// //         <View style={styles.inputContainer}>
// //           <Text style={styles.label}>Rent:</Text>
// //           <TextInput
// //             value={rent}
// //             onChangeText={setRent}
// //             style={styles.input}
// //             keyboardType="numeric"
// //           />
// //         </View>

// //         <View style={styles.inputContainer}>
// //           <Text style={styles.label}>Rooms:</Text>
// //           <TextInput
// //             value={rooms}
// //             onChangeText={setRooms}
// //             style={styles.input}
// //             keyboardType="numeric"
// //           />
// //         </View>

// //         <Text style={styles.label}>Photos:</Text>
// //         <View style={styles.photosContainer}>
// //           {renderPhotos()}
// //           {photos.length < 8 && (
// //             <Button onPress={handleAddPhoto}>Add Photo</Button>
// //           )}
// //         </View>

// //         <Button mode="contained" onPress={handleSubmit} style={styles.submitButton}>
// //           Submit
// //         </Button>

// //         {/* Add some space at the bottom to scroll down */}
// //         <View style={styles.bottomSpace} />
// //       </ScrollView>
// //     </KeyboardAvoidingView>
// //   );
// // };

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     padding: 16,
// //   },
// //   title: {
// //     fontSize: 18,
// //     fontWeight: 'bold',
// //     marginBottom: 16,
// //   },
// //   inputContainer: {
// //     marginBottom: 16,
// //   },
// //   label: {
// //     fontSize: 16,
// //     fontWeight: 'bold',
// //     marginBottom: 8,
// //   },
// //   input: {
// //     height: 40,
// //     borderColor: 'gray',
// //     borderWidth: 1,
// //     paddingHorizontal: 10,
// //   },
// //   photosContainer: {
// //     flexDirection: 'row',
// //     flexWrap: 'wrap',
// //     marginBottom: 16,
// //   },
// //   photoContainer: {
// //     marginRight: 8,
// //     marginBottom: 8,
// //   },
// //   photo: {
// //     width: 80,
// //     height: 80,
// //     resizeMode: 'cover',
// //   },
// //   submitButton: {
// //     marginTop: 16,
// //   },
// //   bottomSpace: {
// //     height: 100, // Adjust the height as needed
// //   },
// // });

// // export default SuccessRoommate;


// // import React, { useState } from 'react';
// // import { View, StyleSheet, Text, TextInput, ScrollView, Image, KeyboardAvoidingView } from 'react-native';
// // import { Button } from 'react-native-paper';
// // import { Picker } from '@react-native-picker/picker';
// // import SelectImageButton from './UploadPhoto'; // Import the UploadPhoto component

// // const countryList = [
// //   { label: 'Select country', value: '' },
// //   { label: 'Country 1', value: 'country1' },
// //   { label: 'Country 2', value: 'country2' },
// //   // Add more countries here
// // ];

// // const SuccessRoommate = () => {
// //   const [country, setCountry] = useState('');
// //   const [city, setCity] = useState('');
// //   const [neighborhood, setNeighborhood] = useState('');
// //   const [street, setStreet] = useState('');
// //   const [apartmentNumber, setApartmentNumber] = useState('');
// //   const [floorNumber, setFloorNumber] = useState('');
// //   const [description, setDescription] = useState('');
// //   const [rent, setRent] = useState('');
// //   const [rooms, setRooms] = useState('');
// //   const [photos, setPhotos] = useState([]);

// //   const handleAddPhoto = (selectedImage) => {
// //     setPhotos([...photos, selectedImage]);
// //   };

// //   const handleRemovePhoto = (index) => {
// //     const updatedPhotos = [...photos];
// //     updatedPhotos.splice(index, 1);
// //     setPhotos(updatedPhotos);
// //   };

// //   const renderPhotos = () => {
// //     return photos.map((photo, index) => (
// //       <View key={index} style={styles.photoContainer}>
// //         <Image source={{ uri: photo }} style={styles.photo} />
// //         <Button onPress={() => handleRemovePhoto(index)}>Remove</Button>
// //       </View>
// //     ));
// //   };

// //   const handleSubmit = () => {
// //     // Implement logic to submit property details
// //     // ...
// //   };

// //   return (
// //     <KeyboardAvoidingView style={styles.container} behavior="padding">
// //       <ScrollView>
// //         <Text style={styles.title}>Enter your property details please</Text>

// //         <View style={styles.rowContainer}>
// //           <View style={styles.inputContainer}>
// //             <Text style={styles.label}>Country:</Text>
// //             <Picker selectedValue={country} onValueChange={setCountry}>
// //               {countryList.map((item, index) => (
// //                 <Picker.Item key={index} label={item.label} value={item.value} />
// //               ))}
// //             </Picker>
// //           </View>

// //           <View style={styles.inputContainer}>
// //             <Text style={styles.label}>City:</Text>
// //             <TextInput
// //               value={city}
// //               onChangeText={setCity}
// //               style={styles.input}
// //             />
// //           </View>
// //         </View>

// //         <View style={styles.rowContainer}>
// //           <View style={styles.inputContainer}>
// //             <Text style={styles.label}>Neighborhood:</Text>
// //             <TextInput
// //               value={neighborhood}
// //               onChangeText={setNeighborhood}
// //               style={styles.input}
// //             />
// //           </View>

// //           <View style={styles.inputContainer}>
// //             <Text style={styles.label}>Street:</Text>
// //             <TextInput
// //               value={street}
// //               onChangeText={setStreet}
// //               style={styles.input}
// //             />
// //           </View>
// //         </View>

// //         <View style={styles.rowContainer}>
// //           <View style={styles.inputContainer}>
// //             <Text style={styles.label}>Apartment Number:</Text>
// //             <TextInput
// //               value={apartmentNumber}
// //               onChangeText={setApartmentNumber}
// //               style={styles.input}
// //             />
// //           </View>

// //           <View style={styles.inputContainer}>
// //             <Text style={styles.label}>Floor Number:</Text>
// //             <TextInput
// //               value={floorNumber}
// //               onChangeText={setFloorNumber}
// //               style={styles.input}
// //             />
// //           </View>
// //         </View>

// //         <View style={styles.rowContainer}>
// //           <View style={styles.inputContainer}>
// //             <Text style={styles.label}>Description:</Text>
// //             <TextInput
// //               multiline
// //               numberOfLines={6}
// //               value={description}
// //               onChangeText={setDescription}
// //               style={[styles.input, { height: 120 }]}
// //             />
// //           </View>
// //         </View>

// //         <View style={styles.rowContainer}>
// //           <View style={styles.inputContainer}>
// //             <Text style={styles.label}>Rent:</Text>
// //             <TextInput
// //               value={rent}
// //               onChangeText={setRent}
// //               style={styles.input}
// //               keyboardType="numeric"
// //             />
// //           </View>

// //           <View style={styles.inputContainer}>
// //             <Text style={styles.label}>Rooms Number:</Text>
// //             <TextInput
// //               value={rooms}
// //               onChangeText={setRooms}
// //               style={styles.input}
// //               keyboardType="numeric"
// //             />
// //           </View>
// //         </View>

// //         <Text style={styles.label}>Photos:</Text>
// //         <View style={styles.photosContainer}>
// //           {renderPhotos()}
// //           <SelectImageButton onImageSelect={handleAddPhoto} />
// //         </View>

// //         <Button mode="contained" onPress={handleSubmit} style={styles.submitButton}>
// //           Submit
// //         </Button>
// //         <View style={{ height: 20 }}></View>
// //       </ScrollView>
// //     </KeyboardAvoidingView>
// //   );
// // };

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     padding: 16,
// //   },
// //   title: {
// //     fontSize: 18,
// //     fontWeight: 'bold',
// //     marginBottom: 40,
// //   },
// //   rowContainer: {
// //     flexDirection: 'row',
// //     justifyContent: 'space-between',
// //     marginBottom: 16,
// //   },
// //   inputContainer: {
// //     flex: 1,
// //     marginRight: 8,
// //   },
// //   label: {
// //     fontSize: 14,
// //     marginBottom: 8,
// //   },
// //   input: {
// //     height: 40,
// //     borderColor: 'gray',
// //     borderWidth: 1,
// //     paddingHorizontal: 10,
// //   },
// //   photosContainer: {
// //     flexDirection: 'row',
// //     flexWrap: 'wrap',
// //     marginBottom: 16,
// //   },
// //   photoContainer: {
// //     marginRight: 8,
// //     marginBottom: 8,
// //   },
// //   photo: {
// //     width: 80,
// //     height: 80,
// //     resizeMode: 'cover',
// //   },
// //   submitButton: {
// //     marginTop: 16,
// //   },
// // });

// // export default SuccessRoommate;



// ###### the best ! -1

// import React, { useState } from 'react';
// import { View, StyleSheet, Text, TextInput, ScrollView, Image, KeyboardAvoidingView } from 'react-native';
// import { Button } from 'react-native-paper';
// import { Picker } from '@react-native-picker/picker';
// import UploadPhotoComp from './UploadPhotoComp';

// // Import the necessary dependencies from React Navigation
// import { useNavigation } from '@react-navigation/native';

// const countryList = [
//   { label: 'Select country', value: '' },
//   { label: 'Country 1', value: 'country1' },
//   { label: 'Country 2', value: 'country2' },
//   // Add more countries here
// ];

// const SuccessRoommate = () => {
//   const navigation = useNavigation(); // Hook to access navigation object

//   const [country, setCountry] = useState('');
//   const [city, setCity] = useState('');
//   const [neighborhood, setNeighborhood] = useState('');
//   const [street, setStreet] = useState('');
//   const [apartmentNumber, setApartmentNumber] = useState('');
//   const [floorNumber, setFloorNumber] = useState('');
//   const [description, setDescription] = useState('');
//   const [rent, setRent] = useState('');
//   const [rooms, setRooms] = useState('');
//   const [photos, setPhotos] = useState([]);

//   const handleAddPhoto = (selectedImage) => {
//     setPhotos([...photos, selectedImage]);
//   };

//   const handleRemovePhoto = (index) => {
//     const updatedPhotos = [...photos];
//     updatedPhotos.splice(index, 1);
//     setPhotos(updatedPhotos);
//   };

//   const renderPhotos = () => {
//     return (
//       <View style={styles.photosContainer}>
//         {photos.map((photo, index) => (
//           <View key={index} style={styles.photoContainer}>
//             <Image source={{ uri: photo }} style={styles.photo} />
//             <Button onPress={() => handleRemovePhoto(index)}>Remove</Button>
//           </View>
//         ))}
//       </View>
//     );
//   };

//   const handleSubmit = () => {
//     // Log the data to the console
//     console.log('Submitted Data:');
//     console.log('Country:', country);
//     console.log('City:', city);
//     console.log('Neighborhood:', neighborhood);
//     console.log('Street:', street);
//     console.log('Apartment Number:', apartmentNumber);
//     console.log('Floor Number:', floorNumber);
//     console.log('Description:', description);
//     console.log('Rent:', rent);
//     console.log('Rooms Number:', rooms);
//     console.log('Photos:', photos);

//     navigation.navigate('IdealRoommate'); // Navigate to the IdealRoommate screen
//   };

//   return (
//     <KeyboardAvoidingView style={styles.container} behavior="padding">
//       <ScrollView>
//         <Text style={styles.title}>Enter your property details please</Text>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Country:</Text>
//             <Picker selectedValue={country} onValueChange={setCountry}>
//               {countryList.map((item, index) => (
//                 <Picker.Item key={index} label={item.label} value={item.value} />
//               ))}
//             </Picker>
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>City:</Text>
//             <TextInput
//               value={city}
//               onChangeText={setCity}
//               style={styles.input}
//             />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Neighborhood:</Text>
//             <TextInput
//               value={neighborhood}
//               onChangeText={setNeighborhood}
//               style={styles.input}
//             />
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Street:</Text>
//             <TextInput
//               value={street}
//               onChangeText={setStreet}
//               style={styles.input}
//             />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Apartment Number:</Text>
//             <TextInput
//               value={apartmentNumber}
//               onChangeText={setApartmentNumber}
//               style={styles.input}
//             />
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Floor Number:</Text>
//             <TextInput
//               value={floorNumber}
//               onChangeText={setFloorNumber}
//               style={styles.input}
//             />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Description:</Text>
//             <TextInput
//               multiline
//               numberOfLines={6}
//               value={description}
//               onChangeText={setDescription}
//               style={[styles.input, { height: 120 }]}
//             />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Rent:</Text>
//             <TextInput
//               value={rent}
//               onChangeText={setRent}
//               style={styles.input}
//               keyboardType="numeric"
//             />
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Rooms Number:</Text>
//             <TextInput
//               value={rooms}
//               onChangeText={setRooms}
//               style={styles.input}
//               keyboardType="numeric"
//             />
//           </View>
//         </View>

//         <Text style={styles.label}>Photos:</Text>
//         {renderPhotos()}
//         <UploadPhotoComp onImageSelect={handleAddPhoto} />

//         <Button mode="contained" onPress={handleSubmit} style={styles.submitButton}>
//           Submit
//         </Button>
//         <View style={{ height: 20 }}></View>
//       </ScrollView>
//     </KeyboardAvoidingView>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     padding: 16,
//   },
//   title: {
//     fontSize: 18,
//     fontWeight: 'bold',
//     marginBottom: 40,
//   },
//   rowContainer: {
//     flexDirection: 'row',
//     justifyContent: 'space-between',
//     marginBottom: 16,
//   },
//   inputContainer: {
//     flex: 1,
//     marginRight: 8,
//   },
//   label: {
//     fontSize: 14,
//     marginBottom: 8,
//   },
//   input: {
//     height: 40,
//     borderColor: 'gray',
//     borderWidth: 1,
//     paddingHorizontal: 10,
//   },
//   photosContainer: {
//     flexDirection: 'row',
//     flexWrap: 'wrap',
//     marginBottom: 16,
//   },
//   photoContainer: {
//     marginRight: 8,
//     marginBottom: 8,
//   },
//   photo: {
//     width: 80,
//     height: 80,
//     resizeMode: 'cover',
//   },
//   submitButton: {
//     marginTop: 16,
//   },
// });

// export default SuccessRoommate;





// import React, { useState } from 'react';
// import { View, StyleSheet, Text, TextInput, ScrollView, Image, KeyboardAvoidingView } from 'react-native';
// import { Button, Checkbox } from 'react-native-paper';
// import { Picker } from '@react-native-picker/picker';
// import UploadPhotoComp from './UploadPhotoComp';

// // Import the necessary dependencies from React Navigation
// import { useNavigation } from '@react-navigation/native';

// const countryList = [
//   { label: 'Select country', value: '' },
//   { label: 'Country 1', value: 'country1' },
//   { label: 'Country 2', value: 'country2' },
//   // Add more countries here
// ];

// const SuccessRoommate = () => {
//   const navigation = useNavigation(); // Hook to access navigation object

//   const [country, setCountry] = useState('');
//   const [city, setCity] = useState('');
//   const [neighborhood, setNeighborhood] = useState('');
//   const [street, setStreet] = useState('');
//   const [apartmentNumber, setApartmentNumber] = useState('');
//   const [floorNumber, setFloorNumber] = useState('');
//   const [description, setDescription] = useState('');
//   const [rent, setRent] = useState('');
//   const [rooms, setRooms] = useState('');
//   const [photos, setPhotos] = useState([]);
//   const [renovated, setRenovated] = useState(false);
//   const [shelter, setShelter] = useState('');
//   const [furnished, setFurnished] = useState(false);
//   const [hasLivingRoom, setHasLivingRoom] = useState(false);
//   const [numOfRooms, setNumOfRooms] = useState('');
//   const [numOfShowers, setNumOfShowers] = useState('');
//   const [numOfRoommates, setNumOfRoommates] = useState('');
//   const [numOfToilets, setNumOfToilets] = useState('');
//   const [nearbyOptions, setNearbyOptions] = useState({
//     supermarket: false,
//     bakery: false,
//     synagogue: false,
//     clinic: false,
//     bars: false,
//     restaurants: false,
//     university: false,
//     school: false,
//     kindergarten: false,
//     mall: false,
//   });

//   const handleAddPhoto = (selectedImage) => {
//     setPhotos([...photos, selectedImage]);
//   };

//   const handleRemovePhoto = (index) => {
//     const updatedPhotos = [...photos];
//     updatedPhotos.splice(index, 1);
//     setPhotos(updatedPhotos);
//   };

//   const handleNearbyOptionChange = (option) => {
//     setNearbyOptions({ ...nearbyOptions, [option]: !nearbyOptions[option] });
//   };

//   const renderPhotos = () => {
//     return (
//       <View style={styles.photosContainer}>
//         {photos.map((photo, index) => (
//           <View key={index} style={styles.photoContainer}>
//             <Image source={{ uri: photo }} style={styles.photo} />
//             <Button onPress={() => handleRemovePhoto(index)}>Remove</Button>
//           </View>
//         ))}
//       </View>
//     );
//   };

//   const handleSubmit = () => {
//     // Log the data to the console
//     console.log('Submitted Data:');
//     console.log('Country:', country);
//     console.log('City:', city);
//     console.log('Neighborhood:', neighborhood);
//     console.log('Street:', street);
//     console.log('Apartment Number:', apartmentNumber);
//     console.log('Floor Number:', floorNumber);
//     console.log('Description:', description);
//     console.log('Rent:', rent);
//     console.log('Rooms Number:', rooms);
//     console.log('Photos:', photos);
//     console.log('Is the property renovated?', renovated);
//     console.log('Is there a shelter?', shelter);
//     console.log('Is the property furnished?', furnished);
//     console.log('Is there a shared living room?', hasLivingRoom);
//     console.log('Number of rooms:', numOfRooms);
//     console.log('Number of showers:', numOfShowers);
//     console.log('Number of roommates:', numOfRoommates);
//     console.log('Number of toilets:', numOfToilets);
//     console.log('Nearby options:', nearbyOptions);

//     navigation.navigate('IdealRoommate'); // Navigate to the IdealRoommate screen
//   };

//   return (
//     <KeyboardAvoidingView style={styles.container} behavior="padding">
//       <ScrollView>
//         <Text style={styles.title}>Enter your property details please</Text>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Country:</Text>
//             <Picker selectedValue={country} onValueChange={setCountry}>
//               {countryList.map((item, index) => (
//                 <Picker.Item key={index} label={item.label} value={item.value} />
//               ))}
//             </Picker>
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>City:</Text>
//             <TextInput value={city} onChangeText={setCity} style={styles.input} />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Neighborhood:</Text>
//             <TextInput
//               value={neighborhood}
//               onChangeText={setNeighborhood}
//               style={styles.input}
//             />
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Street:</Text>
//             <TextInput value={street} onChangeText={setStreet} style={styles.input} />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Apartment Number:</Text>
//             <TextInput
//               value={apartmentNumber}
//               onChangeText={setApartmentNumber}
//               style={styles.input}
//             />
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Floor Number:</Text>
//             <TextInput value={floorNumber} onChangeText={setFloorNumber} style={styles.input} />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Description:</Text>
//             <TextInput
//               multiline
//               numberOfLines={6}
//               value={description}
//               onChangeText={setDescription}
//               style={[styles.input, { height: 120 }]}
//             />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Rent:</Text>
//             <TextInput
//               value={rent}
//               onChangeText={setRent}
//               style={styles.input}
//               keyboardType="numeric"
//             />
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Rooms Number:</Text>
//             <TextInput
//               value={rooms}
//               onChangeText={setRooms}
//               style={styles.input}
//               keyboardType="numeric"
//             />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <Text style={styles.label}>Is the property renovated?</Text>
//           <View style={styles.checkboxContainer}>
//             <CheckBox value={renovated} onValueChange={setRenovated} />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <Text style={styles.label}>Is there a shelter?</Text>
//           <View style={styles.checkboxContainer}>
//             <CheckBox value={shelter} onValueChange={setShelter} />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <Text style={styles.label}>Is the property furnished?</Text>
//           <View style={styles.checkboxContainer}>
//             <CheckBox value={furnished} onValueChange={setFurnished} />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <Text style={styles.label}>Is there a shared living room?</Text>
//           <View style={styles.checkboxContainer}>
//             <CheckBox value={hasLivingRoom} onValueChange={setHasLivingRoom} />
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Number of rooms:</Text>
//             <Picker selectedValue={numOfRooms} onValueChange={setNumOfRooms}>
//               {roomOptions.map((option, index) => (
//                 <Picker.Item key={index} label={option} value={option} />
//               ))}
//             </Picker>
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Number of showers:</Text>
//             <Picker selectedValue={numOfShowers} onValueChange={setNumOfShowers}>
//               {showerOptions.map((option, index) => (
//                 <Picker.Item key={index} label={option} value={option} />
//               ))}
//             </Picker>
//           </View>
//         </View>

//         <View style={styles.rowContainer}>
//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Number of roommates:</Text>
//             <Picker selectedValue={numOfRoommates} onValueChange={setNumOfRoommates}>
//               {roommateOptions.map((option, index) => (
//                 <Picker.Item key={index} label={option} value={option} />
//               ))}
//             </Picker>
//           </View>

//           <View style={styles.inputContainer}>
//             <Text style={styles.label}>Number of toilets:</Text>
//             <Picker selectedValue={numOfToilets} onValueChange={setNumOfToilets}>
//               {toiletOptions.map((option, index) => (
//                 <Picker.Item key={index} label={option} value={option} />
//               ))}
//             </Picker>
//           </View>
//         </View>

//         <Text style={styles.label}>What is available near the apartment?</Text>
//         <View style={styles.checkboxesContainer}>
//           {nearbyOptions.map((option, index) => (
//             <View key={index} style={styles.checkboxContainer}>
//               <CheckBox value={option.selected} onValueChange={() => toggleNearbyOption(index)} />
//               <Text>{option.label}</Text>
//             </View>
//           ))}
//         </View>

//         <Text style={styles.label}>Photos:</Text>
//         {renderPhotos()}
//         <UploadPhotoComp onImageSelect={handleAddPhoto} />

//         <Button mode="contained" onPress={handleSubmit} style={styles.submitButton}>
//           Submit
//         </Button>
//         <View style={{ height: 20 }}></View>
//       </ScrollView>
//     </KeyboardAvoidingView>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     padding: 16,
//     backgroundColor: '#fff',
//   },
//   title: {
//     fontSize: 24,
//     fontWeight: 'bold',
//     marginBottom: 16,
//   },
//   rowContainer: {
//     flexDirection: 'row',
//     marginBottom: 16,
//   },
//   inputContainer: {
//     flex: 1,
//     marginRight: 8,
//   },
//   label: {
//     fontSize: 16,
//     marginBottom: 8,
//   },
//   input: {
//     borderWidth: 1,
//     borderColor: '#ccc',
//     borderRadius: 4,
//     padding: 8,
//   },
//   checkboxContainer: {
//     flexDirection: 'row',
//     alignItems: 'center',
//     marginBottom: 8,
//   },
//   checkboxesContainer: {
//     marginBottom: 16,
//   },
//   photoContainer: {
//     marginBottom: 8,
//   },
//   photo: {
//     width: 100,
//     height: 100,
//     marginRight: 8,
//   },
//   submitButton: {
//     marginTop: 16,
//   },
// });

// export default SuccessRoommate;



// import React, { useState } from 'react';
// import { View, Text, TextInput, Button, StyleSheet, KeyboardAvoidingView, ScrollView } from 'react-native';
// import { Picker } from '@react-native-picker/picker';

// const SuccessRoommate = () => {
//   const [shelter, setShelter] = useState('');
//   const [furnished, setFurnished] = useState('');
//   const [hasLivingRoom, setHasLivingRoom] = useState('');
//   const [numOfRooms, setNumOfRooms] = useState('');
//   const [numOfShowers, setNumOfShowers] = useState('');
//   const [numOfRoommates, setNumOfRoommates] = useState('');
//   const [numOfToilets, setNumOfToilets] = useState('');
//   const [nearbyOptions, setNearbyOptions] = useState({
//     supermarket: '',
//     bakery: '',
//     synagogue: '',
//     clinic: '',
//     bars: '',
//     restaurants: '',
//     university: '',
//     school: '',
//     kindergarten: '',
//     mall: '',
//   });

//   const handleSubmit = () => {
//     // Handle form submission here
//   };

//   return (
//     <ScrollView>
//       <KeyboardAvoidingView behavior="padding" style={styles.container}>
//         <View style={styles.form}>
//           <Text style={styles.heading}>Roommate Preferences</Text>

//           <Text style={styles.label}>Shelter</Text>
//           <TextInput
//             style={styles.input}
//             placeholder="Enter Yes or No"
//             value={shelter}
//             onChangeText={(text) => setShelter(text)}
//           />

//           <Text style={styles.label}>Furnished</Text>
//           <TextInput
//             style={styles.input}
//             placeholder="Enter Yes or No"
//             value={furnished}
//             onChangeText={(text) => setFurnished(text)}
//           />

//           <Text style={styles.label}>Has Living Room</Text>
//           <TextInput
//             style={styles.input}
//             placeholder="Enter Yes or No"
//             value={hasLivingRoom}
//             onChangeText={(text) => setHasLivingRoom(text)}
//           />

//           <Text style={styles.label}>Number of Rooms</Text>
//           <TextInput
//             style={styles.input}
//             placeholder="Enter the number of rooms"
//             value={numOfRooms}
//             onChangeText={(text) => setNumOfRooms(text)}
//             keyboardType="numeric"
//           />

//           <Text style={styles.label}>Number of Showers</Text>
//           <TextInput
//             style={styles.input}
//             placeholder="Enter the number of showers"
//             value={numOfShowers}
//             onChangeText={(text) => setNumOfShowers(text)}
//             keyboardType="numeric"
//           />

//           <Text style={styles.label}>Number of Roommates</Text>
//           <TextInput
//             style={styles.input}
//             placeholder="Enter the number of roommates"
//             value={numOfRoommates}
//             onChangeText={(text) => setNumOfRoommates(text)}
//             keyboardType="numeric"
//           />

//           <Text style={styles.label}>Number of Toilets</Text>
//           <TextInput
//             style={styles.input}
//             placeholder="Enter the number of toilets"
//             value={numOfToilets}
//             onChangeText={(text) => setNumOfToilets(text)}
//             keyboardType="numeric"
//           />

//           <Text style={styles.label}>Nearby Options</Text>
//           <View style={styles.picker}>
//             <Text style={styles.label}>Supermarket</Text>
//             <Picker
//               style={styles.input}
//               selectedValue={nearbyOptions.supermarket}
//               onValueChange={(itemValue) =>
//                 setNearbyOptions((prevOptions) => ({
//                   ...prevOptions,
//                   supermarket: itemValue,
//                 }))
//               }
//             >
//               <Picker.Item label="Yes" value="Yes" />
//               <Picker.Item label="No" value="No" />
//             </Picker>

//             <Text style={styles.label}>Bakery</Text>
//             <Picker
//               style={styles.input}
//               selectedValue={nearbyOptions.bakery}
//               onValueChange={(itemValue) =>
//                 setNearbyOptions((prevOptions) => ({
//                   ...prevOptions,
//                   bakery: itemValue,
//                 }))
//               }
//             >
//               <Picker.Item label="Yes" value="Yes" />
//               <Picker.Item label="No" value="No" />
//             </Picker>

//             <Text style={styles.label}>Synagogue</Text>
//             <Picker
//               style={styles.input}
//               selectedValue={nearbyOptions.synagogue}
//               onValueChange={(itemValue) =>
//                 setNearbyOptions((prevOptions) => ({
//                   ...prevOptions,
//                   synagogue: itemValue,
//                 }))
//               }
//             >
//               <Picker.Item label="Yes" value="Yes" />
//               <Picker.Item label="No" value="No" />
//             </Picker>

//             {/* Add more dropdown menus for other nearby options */}

//             <Text style={styles.label}>Mall</Text>
//             <Picker
//               style={styles.input}
//               selectedValue={nearbyOptions.mall}
//               onValueChange={(itemValue) =>
//                 setNearbyOptions((prevOptions) => ({
//                   ...prevOptions,
//                   mall: itemValue,
//                 }))
//               }
//             >
//               <Picker.Item label="Yes" value="Yes" />
//               <Picker.Item label="No" value="No" />
//             </Picker>
//           </View>

//           <Button mode="contained" onPress={handleSubmit} style={styles.button} title="Submit" />
//         </View>
//       </KeyboardAvoidingView>
//     </ScrollView>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flexGrow: 1,
//     padding: 16,
//   },
//   heading: {
//     fontSize: 24,
//     fontWeight: 'bold',
//     marginBottom: 16,
//   },
//   form: {
//     marginBottom: 32,
//   },
//   label: {
//     fontSize: 16,
//     fontWeight: 'bold',
//     marginBottom: 8,
//   },
//   input: {
//     height: 40,
//     borderColor: 'gray',
//     borderWidth: 1,
//     marginBottom: 16,
//     paddingHorizontal: 8,
//   },
//   picker: {
//     marginBottom: 16,
//   },
//   button: {
//     marginTop: 16,
//   },
//   photosContainer: {
//     flexDirection: 'row',
//     flexWrap: 'wrap',
//     marginBottom: 16,
//   },
//   photoContainer: {
//     marginRight: 8,
//     marginBottom: 8,
//   },
//   photo: {
//     width: 100,
//     height: 100,
//   },
// });

// export default SuccessRoommate;


import React, { useState } from 'react';
import { View, StyleSheet, Text, TextInput, ScrollView, Image, KeyboardAvoidingView } from 'react-native';
import { Button } from 'react-native-paper';
import { Picker } from '@react-native-picker/picker';
import UploadPhotoComp from './UploadPhotoComp';

// Import the necessary dependencies from React Navigation
import { useNavigation } from '@react-navigation/native';

const countryList = [
  { label: 'Select country', value: '' },
  { label: 'Afghanistan', value: 'Afghanistan' },
  { label: 'Albania', value: 'Albania' },
  { label: 'Algeria', value: 'Algeria' },
  { label: 'Andorra', value: 'Andorra' },
  { label: 'Angola', value: 'Angola' },
  { label: 'Antigua and Barbuda', value: 'Antigua and Barbuda' },
  { label: 'Argentina', value: 'Argentina' },
  { label: 'Armenia', value: 'Armenia' },
  { label: 'Australia', value: 'Australia' },
  { label: 'Austria', value: 'Austria' },
  { label: 'Azerbaijan', value: 'Azerbaijan' },
  { label: 'The Bahamas', value: 'The Bahamas' },
  { label: 'Bahrain', value: 'Bahrain' },
  { label: 'Bangladesh', value: 'Bangladesh' },
  { label: 'Barbados', value: 'Barbados' },
  { label: 'Belarus', value: 'Belarus' },
  { label: 'Belgium', value: 'Belgium' },
  { label: 'Belize', value: 'Belize' },
  { label: 'Benin', value: 'Benin' },
  { label: 'Bhutan', value: 'Bhutan' },
  { label: 'Bolivia', value: 'Bolivia' },
  { label: 'Bosnia and Herzegovina', value: 'Bosnia and Herzegovina' },
  { label: 'Botswana', value: 'Botswana' },
  { label: 'Brazil', value: 'Brazil' },
  { label: 'Brunei', value: 'Brunei' },
  { label: 'Bulgaria', value: 'Bulgaria' },
  { label: 'Burkina Faso', value: 'Burkina Faso' },
  { label: 'Burundi', value: 'Burundi' },
  { label: 'Cabo Verde', value: 'Cabo Verde' },
  { label: 'Cambodia', value: 'Cambodia' },
  { label: 'Cameroon', value: 'Cameroon' },
  { label: 'Canada', value: 'Canada' },
  { label: 'Central African Republic', value: 'Central African Republic' },
  { label: 'Chad', value: 'Chad' },
  { label: 'Chile', value: 'Chile' },
  { label: 'China', value: 'China' },
  { label: 'Colombia', value: 'Colombia' },
  { label: 'Comoros', value: 'Comoros' },
  { label: 'Congo, Democratic Republic of the', value: 'Congo, Democratic Republic of the' },
  { label: 'Congo, Republic of the', value: 'Congo, Republic of the' },
  { label: 'Costa Rica', value: 'Costa Rica' },
  { label: 'Côte d’Ivoire', value: 'Côte d’Ivoire' },
  { label: 'Croatia', value: 'Croatia' },
  { label: 'Cuba', value: 'Cuba' },
  { label: 'Cyprus', value: 'Cyprus' },
  { label: 'Czech Republic', value: 'Czech Republic' },
  { label: 'Denmark', value: 'Denmark' },
  { label: 'Djibouti', value: 'Djibouti' },
  { label: 'Dominica', value: 'Dominica' },
  { label: 'Dominican Republic', value: 'Dominican Republic' },
  { label: 'East Timor (Timor-Leste)', value: 'East Timor (Timor-Leste)' },
  { label: 'Ecuador', value: 'Ecuador' },
  { label: 'Egypt', value: 'Egypt' },
  { label: 'El Salvador', value: 'El Salvador' },
  { label: 'Equatorial Guinea', value: 'Equatorial Guinea' },
  { label: 'Eritrea', value: 'Eritrea' },
  { label: 'Estonia', value: 'Estonia' },
  { label: 'Eswatini', value: 'Eswatini' },
  { label: 'Ethiopia', value: 'Ethiopia' },
  { label: 'Fiji', value: 'Fiji' },
  { label: 'Finland', value: 'Finland' },
  { label: 'France', value: 'France' },
  { label: 'Gabon', value: 'Gabon' },
  { label: 'The Gambia', value: 'The Gambia' },
  { label: 'Georgia', value: 'Georgia' },
  { label: 'Germany', value: 'Germany' },
  { label: 'Ghana', value: 'Ghana' },
  { label: 'Greece', value: 'Greece' },
  { label: 'Grenada', value: 'Grenada' },
  { label: 'Guatemala', value: 'Guatemala' },
  { label: 'Guinea', value: 'Guinea' },
  { label: 'Guinea-Bissau', value: 'Guinea-Bissau' },
  { label: 'Guyana', value: 'Guyana' },
  { label: 'Haiti', value: 'Haiti' },
  { label: 'Honduras', value: 'Honduras' },
  { label: 'Hungary', value: 'Hungary' },
  { label: 'Iceland', value: 'Iceland' },
  { label: 'India', value: 'India' },
  { label: 'Indonesia', value: 'Indonesia' },
  { label: 'Iran', value: 'Iran' },
  { label: 'Iraq', value: 'Iraq' },
  { label: 'Ireland', value: 'Ireland' },
  { label: 'Israel', value: 'Israel' },
  { label: 'Italy', value: 'Italy' },
  { label: 'Jamaica', value: 'Jamaica' },
  { label: 'Japan', value: 'Japan' },
  { label: 'Jordan', value: 'Jordan' },
  { label: 'Kazakhstan', value: 'Kazakhstan' },
  { label: 'Kenya', value: 'Kenya' },
  { label: 'Kiribati', value: 'Kiribati' },
  { label: 'Korea, North', value: 'Korea, North' },
  { label: 'Korea, South', value: 'Korea, South' },
  { label: 'Kosovo', value: 'Kosovo' },
  { label: 'Kuwait', value: 'Kuwait' },
  { label: 'Kyrgyzstan', value: 'Kyrgyzstan' },
  { label: 'Laos', value: 'Laos' },
  { label: 'Latvia', value: 'Latvia' },
  { label: 'Lebanon', value: 'Lebanon' },
  { label: 'Lesotho', value: 'Lesotho' },
  { label: 'Liberia', value: 'Liberia' },
  { label: 'Libya', value: 'Libya' },
  { label: 'Liechtenstein', value: 'Liechtenstein' },
  { label: 'Lithuania', value: 'Lithuania' },
  { label: 'Luxembourg', value: 'Luxembourg' },
  { label: 'Madagascar', value: 'Madagascar' },
  { label: 'Malawi', value: 'Malawi' },
  { label: 'Malaysia', value: 'Malaysia' },
  { label: 'Maldives', value: 'Maldives' },
  { label: 'Mali', value: 'Mali' },
  { label: 'Malta', value: 'Malta' },
  { label: 'Marshall Islands', value: 'Marshall Islands' },
  { label: 'Mauritania', value: 'Mauritania' },
  { label: 'Mauritius', value: 'Mauritius' },
  { label: 'Mexico', value: 'Mexico' },
  { label: 'Micronesia, Federated States of', value: 'Micronesia, Federated States of' },
  { label: 'Moldova', value: 'Moldova' },
  { label: 'Monaco', value: 'Monaco' },
  { label: 'Mongolia', value: 'Mongolia' },
  { label: 'Montenegro', value: 'Montenegro' },
  { label: 'Morocco', value: 'Morocco' },
  { label: 'Mozambique', value: 'Mozambique' },
  { label: 'Myanmar (Burma)', value: 'Myanmar (Burma)' },
  { label: 'Namibia', value: 'Namibia' },
  { label: 'Nauru', value: 'Nauru' },
  { label: 'Nepal', value: 'Nepal' },
  { label: 'Netherlands', value: 'Netherlands' },
  { label: 'New Zealand', value: 'New Zealand' },
  { label: 'Nicaragua', value: 'Nicaragua' },
  { label: 'Niger', value: 'Niger' },
  { label: 'Nigeria', value: 'Nigeria' },
  { label: 'North Macedonia (Macedonia)', value: 'North Macedonia (Macedonia)' },
  { label: 'Norway', value: 'Norway' },
  { label: 'Oman', value: 'Oman' },
  { label: 'Pakistan', value: 'Pakistan' },
  { label: 'Palau', value: 'Palau' },
  { label: 'Panama', value: 'Panama' },
  { label: 'Papua New Guinea', value: 'Papua New Guinea' },
  { label: 'Paraguay', value: 'Paraguay' },
  { label: 'Peru', value: 'Peru' },
  { label: 'Philippines', value: 'Philippines' },
  { label: 'Poland', value: 'Poland' },
  { label: 'Portugal', value: 'Portugal' },
  { label: 'Qatar', value: 'Qatar' },
  { label: 'Romania', value: 'Romania' },
  { label: 'Russia', value: 'Russia' },
  { label: 'Rwanda', value: 'Rwanda' },
  { label: 'Saint Kitts and Nevis', value: 'Saint Kitts and Nevis' },
  { label: 'Saint Lucia', value: 'Saint Lucia' },
  { label: 'Saint Vincent and the Grenadines', value: 'Saint Vincent and the Grenadines' },
  { label: 'Samoa', value: 'Samoa' },
  { label: 'San Marino', value: 'San Marino' },
  { label: 'Sao Tome and Principe', value: 'Sao Tome and Principe' },
  { label: 'Saudi Arabia', value: 'Saudi Arabia' },
  { label: 'Senegal', value: 'Senegal' },
  { label: 'Serbia', value: 'Serbia' },
  { label: 'Seychelles', value: 'Seychelles' },
  { label: 'Sierra Leone', value: 'Sierra Leone' },
  { label: 'Singapore', value: 'Singapore' },
  { label: 'Slovakia', value: 'Slovakia' },
  { label: 'Slovenia', value: 'Slovenia' },
  { label: 'Solomon Islands', value: 'Solomon Islands' },
  { label: 'Somalia', value: 'Somalia' },
  { label: 'South Africa', value: 'South Africa' },
  { label: 'South Sudan', value: 'South Sudan' },
  { label: 'Spain', value: 'Spain' },
  { label: 'Sri Lanka', value: 'Sri Lanka' },
  { label: 'Sudan', value: 'Sudan' },
  { label: 'Suriname', value: 'Suriname' },
  { label: 'Sweden', value: 'Sweden' },
  { label: 'Switzerland', value: 'Switzerland' },
  { label: 'Syria', value: 'Syria' },
  { label: 'Taiwan', value: 'Taiwan' },
  { label: 'Tajikistan', value: 'Tajikistan' },
  { label: 'Tanzania', value: 'Tanzania' },
  { label: 'Thailand', value: 'Thailand' },
  { label: 'Togo', value: 'Togo' },
  { label: 'Tonga', value: 'Tonga' },
  { label: 'Trinidad and Tobago', value: 'Trinidad and Tobago' },
  { label: 'Tunisia', value: 'Tunisia' },
  { label: 'Turkey', value: 'Turkey' },
  { label: 'Turkmenistan', value: 'Turkmenistan' },
  { label: 'Tuvalu', value: 'Tuvalu' },
  { label: 'Uganda', value: 'Uganda' },
  { label: 'Ukraine', value: 'Ukraine' },
  { label: 'United Arab Emirates', value: 'United Arab Emirates' },
  { label: 'United Kingdom', value: 'United Kingdom' },
  { label: 'United States', value: 'United States' },
  { label: 'Uruguay', value: 'Uruguay' },
  { label: 'Uzbekistan', value: 'Uzbekistan' },
  { label: 'Vanuatu', value: 'Vanuatu' },
  { label: 'Vatican City', value: 'Vatican City' },
  { label: 'Venezuela', value: 'Venezuela' },
  { label: 'Vietnam', value: 'Vietnam' },
  { label: 'Yemen', value: 'Yemen' },
  { label: 'Zambia', value: 'Zambia' },
  { label: 'Zimbabwe', value: 'Zimbabwe' },
];

const cityList = [
  { label: 'Select city', value: '' },
  { label: 'Afula', value: 'Afula' },
  { label: '‘Akko', value: '‘Akko' },
  { label: 'Al Buţayḩah', value: 'Al Buţayḩah' },
  { label: 'Al Khushnīyah', value: 'Al Khushnīyah' },
  { label: 'Ashdod', value: 'Ashdod' },
  { label: 'Ashqelon', value: 'Ashqelon' },
  { label: 'Bat Yam', value: 'Bat Yam' },
  { label: 'Beersheba', value: 'Beersheba' },
  { label: 'Ben Zakkay', value: 'Ben Zakkay' },
  { label: 'Bené Beraq', value: 'Bené Beraq' },
  { label: 'Bet Shemesh', value: 'Bet Shemesh' },
  { label: 'Dimona', value: 'Dimona' },
  { label: 'Eilat', value: 'Eilat' },
  { label: 'El‘ad', value: 'El‘ad' },
  { label: 'Eṭ Ṭaiyiba', value: 'Eṭ Ṭaiyiba' },
  { label: 'Fīq', value: 'Fīq' },
  { label: 'Givatayim', value: 'Givatayim' },
  { label: 'Haifa', value: 'Haifa' },
  { label: 'Hadera', value: 'Hadera' },
  { label: 'Herẕliyya', value: 'Herẕliyya' },
  { label: 'Hod HaSharon', value: 'Hod HaSharon' },
  { label: 'Holon', value: 'Holon' },
  { label: 'Jerusalem', value: 'Jerusalem' },
  { label: 'Karmiel', value: 'Karmiel' },
  { label: 'Kefar Sava', value: 'Kefar Sava' },
  { label: 'Lod', value: 'Lod' },
  { label: 'Ma‘alot Tarshīḥā', value: 'Ma‘alot Tarshīḥā' },
  { label: 'Modi‘in Makkabbim Re‘ut', value: 'Modi‘in Makkabbim Re‘ut' },
  { label: 'Nahariyya', value: 'Nahariyya' },
  { label: 'Nazareth', value: 'Nazareth' },
  { label: 'Nes Ẕiyyona', value: 'Nes Ẕiyyona' },
  { label: 'Netanya', value: 'Netanya' },
  { label: 'Netivot', value: 'Netivot' },
  { label: 'Or Yehuda', value: 'Or Yehuda' },
  { label: 'Pardés H̱anna Karkur', value: 'Pardés H̱anna Karkur' },
  { label: 'Petaẖ Tiqwa', value: 'Petaẖ Tiqwa' },
  { label: 'Qiryat Ata', value: 'Qiryat Ata' },
  { label: 'Qiryat Bialik', value: 'Qiryat Bialik' },
  { label: 'Qiryat Gat', value: 'Qiryat Gat' },
  { label: 'Qiryat Moẕqin', value: 'Qiryat Moẕqin' },
  { label: 'Qiryat Ono', value: 'Qiryat Ono' },
  { label: 'Qiryat Yam', value: 'Qiryat Yam' },
  { label: 'Rahat', value: 'Rahat' },
  { label: 'Ramla', value: 'Ramla' },
  { label: 'Ramat Gan', value: 'Ramat Gan' },
  { label: 'Ramat HaSharon', value: 'Ramat HaSharon' },
  { label: 'Ra‘ananna', value: 'Ra‘ananna' },
  { label: 'Reẖovot', value: 'Reẖovot' },
  { label: 'Rishon LeẔiyyon', value: 'Rishon LeẔiyyon' },
  { label: 'Rosh Ha‘Ayin', value: 'Rosh Ha‘Ayin' },
  { label: 'Sakhnīn', value: 'Sakhnīn' },
  { label: 'Shefar‘am', value: 'Shefar‘am' },
  { label: 'Tamra', value: 'Tamra' },
  { label: 'Tel Aviv-Yafo', value: 'Tel Aviv-Yafo' },
  { label: 'Tiberias', value: 'Tiberias' },
  { label: 'Umm el Faḥm', value: 'Umm el Faḥm' },
  { label: 'Yehud', value: 'Yehud' },
  { label: 'Ẕefat', value: 'Ẕefat' },
];


const SuccessRoommate = () => {
  const navigation = useNavigation(); // Hook to access navigation object

  const [country, setCountry] = useState('');
  const [city, setCity] = useState('');
  const [neighborhood, setNeighborhood] = useState('');
  const [street, setStreet] = useState('');
  const [apartmentNumber, setApartmentNumber] = useState('');
  const [floorNumber, setFloorNumber] = useState('');
  const [description, setDescription] = useState('');
  const [rent, setRent] = useState('');
  const [rooms, setRooms] = useState('');
  const [photos, setPhotos] = useState([]);
  const [isRenovated, setIsRenovated] = useState('');
  const [shelter, setShelter] = useState('');
  const [isFurnished, setIsFurnished] = useState('');
  const [hasLivingRoom, setHasLivingRoom] = useState('');
  const [numberOfRooms, setNumberOfRooms] = useState('');
  const [numberOfShowers, setNumberOfShowers] = useState('');
  const [numberOfRoommates, setNumberOfRoommates] = useState('');
  const [numberOfToilets, setNumberOfToilets] = useState('');
  const [nearbyOptions, setNearbyOptions] = useState({
    supermarket: false,
    bakery: false,
    synagogue: false,
    clinic: false,
    bars: false,
    restaurants: false,
    university: false,
    school: false,
    kindergarten: false,
    mall: false,
  });

  const roomNumbers = [
    '1',
    '1.5',
    '2',
    '2.5',
    '3',
    '3.5',
    '4',
    '4.5',
    '5',
    '5.5',
    '6',
  ];
  
  const showerNumbers = ['1', '2', '3'];
  
  const roommateNumbers = ['1', '2', '3', '4'];
  
  const toiletNumbers = ['1', '2', '3'];

  const nearbyOptionsList = [
    'Supermarket',
    'Bakery',
    'Synagogue',
    'Clinic',
    'Bars',
    'Restaurants',
    'University',
    'School',
    'Kindergarten',
    'Mall/Shopping Center',
  ];
  
  

  const handleAddPhoto = (selectedImage) => {
    setPhotos([...photos, selectedImage]);
  };

  const handleRemovePhoto = (index) => {
    const updatedPhotos = [...photos];
    updatedPhotos.splice(index, 1);
    setPhotos(updatedPhotos);
  };

  const renderPhotos = () => {
    return (
      <View style={styles.photosContainer}>
        {photos.map((photo, index) => (
          <View key={index} style={styles.photoContainer}>
            <Image source={{ uri: photo }} style={styles.photo} />
            <Button onPress={() => handleRemovePhoto(index)}>Remove</Button>
          </View>
        ))}
      </View>
    );
  };

  const handleCountryChange = (value) => {
    setCountry(value);
  };

  const handleCityChange = (value) => {
    setCity(value);
  };

  const handleSubmit = () => {
    // Log the data to the console
    console.log('Submitted Data:');
    console.log('Country:', country);
    console.log('City:', city);
    console.log('Neighborhood:', neighborhood);
    console.log('Street:', street);
    console.log('Apartment Number:', apartmentNumber);
    console.log('Floor Number:', floorNumber);
    console.log('Description:', description);
    console.log('Rent:', rent);
    console.log('Rooms Number:', rooms);
    console.log('Photos:', photos);
    console.log('Is the property renovated?', isRenovated);
    console.log('Is there a shelter?', shelter);
    console.log('Is there a property furnished?', isFurnished);
    console.log('Is there a shared living room?', hasLivingRoom);
    console.log('Number of rooms:', numberOfRooms);
    console.log('Number of showers:', numberOfShowers);
    console.log('Number of roommates:', numberOfRoommates);
    console.log('Number of toilets:', numberOfToilets);
    console.log('Nearby options:', nearbyOptions);

    navigation.navigate('IdealRoommate'); // Navigate to the IdealRoommate screen
  };

  const handleNearbyOptionChange = (option) => {
    setNearbyOptions({ ...nearbyOptions, [option]: !nearbyOptions[option] });
  };

  return (
    <KeyboardAvoidingView style={styles.container} behavior="padding">
      <ScrollView>
        <Text style={styles.title}>Enter your property details please</Text>

        <View style={styles.rowContainer}>
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Country:</Text>
            <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={country} onValueChange={setCountry}>
              {countryList.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>

          <View style={styles.inputContainer}>
            <Text style={styles.label}>City:</Text>
            <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={city} onValueChange={setCity}>
              {cityList.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>
        </View>

        <View style={styles.rowContainer}>
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Neighborhood:</Text>
            <TextInput
              value={neighborhood}
              onChangeText={setNeighborhood}
              style={styles.input}
            />
          </View>

          <View style={styles.inputContainer}>
            <Text style={styles.label}>Street:</Text>
            <TextInput value={street} onChangeText={setStreet} style={styles.input} />
          </View>
        </View>

        <View style={styles.rowContainer}>
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Apartment Number:</Text>
            <TextInput
              value={apartmentNumber}
              onChangeText={setApartmentNumber}
              style={styles.input}
            />
          </View>

          <View style={styles.inputContainer}>
            <Text style={styles.label}>Floor Number:</Text>
            <TextInput
              value={floorNumber}
              onChangeText={setFloorNumber}
              style={styles.input}
            />
          </View>
        </View>

        <View style={styles.rowContainer}>
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Description:</Text>
            <TextInput
              multiline
              numberOfLines={6}
              value={description}
              onChangeText={setDescription}
              style={[styles.input, { height: 120 }]}
            />
          </View>
        </View>

        <View style={styles.rowContainer}>
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Rent:</Text>
            <TextInput
              value={rent}
              onChangeText={setRent}
              style={styles.input}
              keyboardType="numeric"
            />
          </View>

          <View style={styles.inputContainer}>
            <Text style={styles.label}>Square Meters:</Text>
            <TextInput
              value={rooms}
              onChangeText={setRooms}
              style={styles.input}
              keyboardType="numeric"
            />
          </View>
        </View>
      
        <View style={styles.rowContainer}>
          <Text style={styles.label}>Photos: </Text>
          {renderPhotos()}
        </View>
        <View style={styles.rowContainer2}>
          <UploadPhotoComp onImageSelect={handleAddPhoto} />
        </View>

        <Text style={styles.label}>Is the property renovated?</Text>
        <View style={styles.inputContainer}>
          <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={isRenovated} onValueChange={setIsRenovated}>
            <Picker.Item label="Yes" value="yes" />
            <Picker.Item label="No" value="no" />
          </Picker>
        </View>
            
        <Text style={styles.label}>Is there a shelter?</Text>
        <View style={styles.inputContainer}>
          <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={shelter} onValueChange={setShelter}>
            <Picker.Item label="Inside" value="inside" />
            <Picker.Item label="Nearby" value="nearby" />
            <Picker.Item label="No" value="no" />
          </Picker>
        </View>

        <Text style={styles.label}>Is there a property furnished?</Text>
        <View style={styles.inputContainer}>
          <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={isFurnished} onValueChange={setIsFurnished}>
            <Picker.Item label="Yes" value="yes" />
            <Picker.Item label="No" value="no" />
          </Picker>
        </View>

        <Text style={styles.label}>Is there a shared living room?</Text>
        <View style={styles.inputContainer}>
          <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={hasLivingRoom} onValueChange={setHasLivingRoom}>
            <Picker.Item label="Yes" value="yes" />
            <Picker.Item label="No" value="no" />
          </Picker>
        </View>

        <View style={styles.rowContainer}>
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Number of rooms:</Text>
            <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={numberOfRooms} onValueChange={setNumberOfRooms}>
              {roomNumbers.map((number, index) => (
                <Picker.Item key={index} label={number.toString()} value={number.toString()} />
              ))}
            </Picker>
          </View>
          
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Number of roommates:</Text>
            <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={numberOfRoommates} onValueChange={setNumberOfRoommates}>
              {roommateNumbers.map((number, index) => (
                <Picker.Item key={index} label={number.toString()} value={number.toString()} />
              ))}
            </Picker>
          </View>
          
        </View>

        <View style={styles.rowContainer}>
          <View style={styles.inputContainer}>
            <Text style={styles.label}>Number of toilets:</Text>
            <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={numberOfToilets} onValueChange={setNumberOfToilets}>
              {toiletNumbers.map((number, index) => (
                <Picker.Item key={index} label={number.toString()} value={number.toString()} />
              ))}
            </Picker>
          </View>

          <View style={styles.inputContainer}>
              <Text style={styles.label}>Number of showers:</Text>
              <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={numberOfShowers} onValueChange={setNumberOfShowers}>
                {showerNumbers.map((number, index) => (
                  <Picker.Item key={index} label={number.toString()} value={number.toString()} />
                ))}
              </Picker>
            </View>
        </View>

        <Text style={styles.nearbyOptionsLabel}>What is available near the apartment?</Text>
        <View style={styles.nearbyOptionsContainer}>
          {nearbyOptionsList.map((option, index) => (
            <Text
              key={index}
              style={[styles.nearbyOption, nearbyOptions[option] && styles.nearbyOptionSelected]}
              onPress={() => handleNearbyOptionChange(option)}
            >
              {option}
            </Text>
          ))}
        </View>

        <Button mode="contained" onPress={handleSubmit} style={styles.button}>
          Next
        </Button>
      </ScrollView>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 40,
    color: '#8C8CB4',
  },
  rowContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  rowContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  inputContainer: {
    flex: 1,
    marginRight: 10,
  },
  label: {
    fontSize: 16,
    marginBottom: 5,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 4,
    padding: 10,
    fontSize: 16,
  },
  photosContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginBottom: 20,
  },
  photoContainer: {
    marginRight: 10,
    marginBottom: 10,
  },
  photo: {
    width: 100,
    height: 100,
    borderRadius: 4,
  },
  button: {
    marginTop: 20,
    marginBottom: 40,
    paddingVertical: 5,
  },
  nearbyOptionsLabel: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  nearbyOptionsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginBottom: 20,
  },
  nearbyOption: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 4,
    padding: 10,
    marginRight: 10,
    marginBottom: 10,
    backgroundColor: '#fff',
  },
  nearbyOptionSelected: {
    backgroundColor: 'blue',
    color: '#fff',
  },
  pickerItem: {
    fontSize: 18,
  },
});

export default SuccessRoommate;
