// import React, { useState, useEffect } from 'react';
// import { View, StyleSheet } from 'react-native';
// import { TextInput, Button } from 'react-native-paper';
// import PhoneInput from 'react-native-phone-input';
// import DatePicker from 'react-native-datepicker';

// const PersonalInfoScreen = ({ navigation }) => {
//   const [firstName, setFirstName] = useState('');
//   const [lastName, setLastName] = useState('');
//   const [phoneNumber, setPhoneNumber] = useState('');
//   const [birthdate, setBirthdate] = useState('');
//   const [gender, setGender] = useState('');

//   useEffect(() => {
//     // Perform any logic needed when the birthdate changes
//     console.log('Birthdate:', birthdate);
//   }, [birthdate]);

//   const handleNext = () => {
//     // Perform logic with personal info
//     console.log('Personal Info:', {
//       firstName,
//       lastName,
//       phoneNumber,
//       birthdate,
//       gender,
//     });

//     // Navigate to the next screen
//     navigation.navigate('AdditionalInfo');
//   };

//   return (
//     <View style={styles.container}>
//       <TextInput
//         label="First Name"
//         value={firstName}
//         onChangeText={setFirstName}
//         style={styles.input}
//       />
//       <TextInput
//         label="Last Name"
//         value={lastName}
//         onChangeText={setLastName}
//         style={styles.input}
//       />

//       <PhoneInput
//         initialCountry="us"
//         value={phoneNumber}
//         onChangePhoneNumber={setPhoneNumber}
//         textStyle={styles.phoneInput}
//         style={styles.input}
//       />

//       {/* <DatePicker
//         style={styles.input}
//         date={birthdate}
//         mode="date"
//         placeholder="Select Birthdate"
//         format="DD-MM-YYYY"
//         minDate="01-01-1900"
//         maxDate={new Date()}
//         confirmBtnText="Confirm"
//         cancelBtnText="Cancel"
//         customStyles={{
//           dateIcon: {
//             position: 'absolute',
//             left: 0,
//             top: 4,
//             marginLeft: 0,
//           },
//           dateInput: {
//             marginLeft: 36,
//           },
//           // You can customize the styling further if needed
//         }}
//         onDateChange={setBirthdate}
//         useNativeDriver={true} // Set useNativeDriver to true
//       /> */}

//       <TextInput
//         label="Gender"
//         value={gender}
//         onChangeText={setGender}
//         style={styles.input}
//       />

//       <Button mode="contained" onPress={handleNext} style={styles.button}>
//         Next
//       </Button>
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     padding: 16,
//     justifyContent: 'center',
//   },
//   input: {
//     marginBottom: 16,
//   },
//   phoneInput: {
//     fontSize: 16,
//     paddingHorizontal: 16,
//   },
//   button: {
//     marginTop: 16,
//   },
// });

// export default PersonalInfoScreen;


// import React, { useState, useEffect } from 'react';
// import { View, StyleSheet, TouchableWithoutFeedback, Text } from 'react-native';
// import { TextInput, Button } from 'react-native-paper';
// import PhoneInput from 'react-native-phone-input';
// import { format, parse } from 'date-fns';

// const PersonalInfoScreen = ({ navigation }) => {
//   const [firstName, setFirstName] = useState('');
//   const [lastName, setLastName] = useState('');
//   const [phoneNumber, setPhoneNumber] = useState('');
//   const [birthdate, setBirthdate] = useState('');
//   const [gender, setGender] = useState('');
//   const [showDatePicker, setShowDatePicker] = useState(false);
//   const [selectedDate, setSelectedDate] = useState(null);
  

//   const handleDateChange = (text) => {
//     const parsedDate = parse(text, 'yyyy-MM-dd', new Date());
//     if (isValid(parsedDate)) {
//       const formattedDate = format(parsedDate, 'yyyy-MM-dd');
//       setBirthdate(formattedDate);
//     } else {
//       setBirthdate('');
//     }
//   };

//   const isValid = (date) => {
//     return !isNaN(date) && date instanceof Date;
//   };

//   // useEffect(() => {
//   //   // Perform any logic needed when the birthdate changes
//   //   console.log('Birthdate:', birthdate);
//   // }, [birthdate]);

//   const handleNext = () => {
//     // Perform logic with personal info
//     console.log('Personal Info:', {
//       firstName,
//       lastName,
//       phoneNumber,
//       birthdate,
//       gender,
//     });

//     // Navigate to the next screen
//     navigation.navigate('AdditionalInfo');
//   };

//   return (
//     <View style={styles.container}>
//       <TextInput
//         label="First Name"
//         value={firstName}
//         onChangeText={setFirstName}
//         style={styles.input}
//       />
//       <TextInput
//         label="Last Name"
//         value={lastName}
//         onChangeText={setLastName}
//         style={styles.input}
//       />

//       <PhoneInput
//         initialCountry="us"
//         value={phoneNumber}
//         onChangePhoneNumber={setPhoneNumber}
//         textStyle={styles.phoneInput}
//         style={styles.input}
//       />

//       <TextInput
//         label="Birthdate"
//         value={birthdate}
//         onChangeText={handleDateChange}
//         style={styles.input}
//         placeholder="YYYY-MM-DD"
//       />

//       <TextInput
//         label="Gender"
//         value={gender}
//         onChangeText={setGender}
//         style={styles.input}
//       />

//       <Button mode="contained" onPress={handleNext} style={styles.button} disabled={!birthdate}>
//         Next
//       </Button>
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     padding: 16,
//     justifyContent: 'center',
//   },
//   input: {
//     marginBottom: 16,
//     borderWidth: 1,
//     borderColor: 'gray',
//     borderRadius: 4,
//     paddingVertical: 12,
//     paddingHorizontal: 16,
//   },
//   phoneInput: {
//     fontSize: 16,
//     paddingHorizontal: 16,
//   },
//   button: {
//     marginTop: 16,
//   },
//   dateText: {
//     fontSize: 16,
//   },
// });

// export default PersonalInfoScreen;


import React, { useState } from 'react';
import { View, StyleSheet, Image } from 'react-native';
import { TextInput, Button, Text } from 'react-native-paper';
import PhoneInput from 'react-native-phone-input';
import ImagePicker from 'react-native-image-picker';


const PersonalInfoScreen = ({ navigation }) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [birthdateYear, setBirthdateYear] = useState('');
  const [birthdateMonth, setBirthdateMonth] = useState('');
  const [birthdateDay, setBirthdateDay] = useState('');
  const [gender, setGender] = useState('');
  const [selectedImage, setSelectedImage] = useState(null);
  

  const handleImageSelect = async () => {
    const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
    if (status !== 'granted') {
      console.log('Permission to access media library was denied');
      return;
    }
  
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [1, 1],
      quality: 1,
    });
  
    if (!result.cancelled) {
      // Store the selected image
      setSelectedImage(result.uri);
    }
  };
  
  

  const handleNext = () => {
    // Perform logic with personal info
    console.log('Personal Info:', {
      firstName,
      lastName,
      phoneNumber,
      birthdateYear,
      birthdateMonth,
      birthdateDay,
      gender,
    });

    // Navigate to the next screen
    navigation.navigate('UploadPhoto');
  };

  return (
    <View style={styles.container}>
      {selectedImage && <Image source={{ uri: selectedImage }} style={styles.image} />}
       <Button title="Select Image" onPress={handleImageSelect} />
      <TextInput
        label="First Name"
        value={firstName}
        onChangeText={setFirstName}
        style={styles.input}
      />
      <TextInput
        label="Last Name"
        value={lastName}
        onChangeText={setLastName}
        style={styles.input}
      />

      <PhoneInput
        initialCountry="us"
        value={phoneNumber}
        onChangePhoneNumber={setPhoneNumber}
        textStyle={styles.phoneInput}
        style={styles.input}
      />


      <View style={styles.dateContainer}>
        <Text style={styles.label}>Birthdate:                </Text>
        <TextInput
          label="YYYY"
          value={birthdateYear}
          onChangeText={setBirthdateYear}
          style={styles.dateInput}
          placeholder="YYYY"
          keyboardType="numeric"
        />

        <TextInput
          label="MM"
          value={birthdateMonth}
          onChangeText={setBirthdateMonth}
          style={styles.dateInput}
          placeholder="MM"
          keyboardType="numeric"
        />

        <TextInput
          label="DD"
          value={birthdateDay}
          onChangeText={setBirthdateDay}
          style={styles.dateInput}
          placeholder="DD"
          keyboardType="numeric"
        />
      </View>


      <TextInput
        label="Gender"
        value={gender}
        onChangeText={setGender}
        style={styles.input}
      />

      <Button mode="contained" onPress={handleNext} style={styles.button}>
        Next
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    justifyContent: 'center',
  },
  dateContainer: {
    flexDirection: 'row',
    marginBottom: 16,
  },
  dateInput: {
    flex: 1,
    marginRight: 8,
  },
  input: {
    marginBottom: 16,
  },
  phoneInput: {
    fontSize: 16,
    paddingHorizontal: 16,
  },
  button: {
    marginTop: 16,
  },
});

export default PersonalInfoScreen;



// import React, { useState } from 'react';
// import { View, StyleSheet, Image } from 'react-native';
// import { TextInput, Button, Text } from 'react-native-paper';
// import PhoneInput from 'react-native-phone-input';
// import ImagePicker from 'react-native-image-picker';

// const PersonalInfoScreen = ({ navigation }) => {
//   const [firstName, setFirstName] = useState('');
//   const [lastName, setLastName] = useState('');
//   const [phoneNumber, setPhoneNumber] = useState('');
//   const [birthdateYear, setBirthdateYear] = useState('');
//   const [birthdateMonth, setBirthdateMonth] = useState('');
//   const [birthdateDay, setBirthdateDay] = useState('');
//   const [gender, setGender] = useState('');
//   const [selectedImage, setSelectedImage] = useState(null);
//   const [selectedFacebookProfile, setSelectedFacebookProfile] = useState(null);

//   const handleImageSelect = async () => {
//     const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
//     if (status !== 'granted') {
//       console.log('Permission to access media library was denied');
//       return;
//     }

//     const result = await ImagePicker.launchImageLibraryAsync({
//       mediaTypes: ImagePicker.MediaTypeOptions.Images,
//       allowsEditing: true,
//       aspect: [1, 1],
//       quality: 1,
//     });

//     if (!result.cancelled) {
//       // Store the selected image
//       setSelectedImage(result.uri);
//     }
//   };

//   const handleFacebookProfileSelect = () => {
//     // Logic for connecting to Facebook profile
//     console.log('Connect to Facebook profile');
//   };

//   const handleNext = () => {
//     // Perform logic with personal info
//     console.log('Personal Info:', {
//       firstName,
//       lastName,
//       phoneNumber,
//       birthdateYear,
//       birthdateMonth,
//       birthdateDay,
//       gender,
//       selectedFacebookProfile,
//     });

//     // Navigate to the next screen
//     navigation.navigate('UploadPhoto');
//   };

//   return (
//     <View style={styles.container}>
//       {selectedImage && <Image source={{ uri: selectedImage }} style={styles.image} />}
//       <Button mode="contained" onPress={handleImageSelect} style={styles.button}>
//         Select Image
//       </Button>

//       <Button mode="contained" onPress={handleFacebookProfileSelect} style={styles.button}>
//         Connect Facebook
//       </Button>

//       <TextInput
//         label="First Name"
//         value={firstName}
//         onChangeText={setFirstName}
//         style={styles.input}
//       />
//       <TextInput
//         label="Last Name"
//         value={lastName}
//         onChangeText={setLastName}
//         style={styles.input}
//       />

//       <PhoneInput
//         initialCountry="us"
//         value={phoneNumber}
//         onChangePhoneNumber={setPhoneNumber}
//         textStyle={styles.phoneInput}
//         style={styles.input}
//       />

//       <View style={styles.dateContainer}>
//         <TextInput
//           label="YYYY"
//           value={birthdateYear}
//           onChangeText={setBirthdateYear}
//           style={styles.dateInput}
//           placeholder="YYYY"
//           keyboardType="numeric"
//         />

//         <TextInput
//           label="MM"
//           value={birthdateMonth}
//           onChangeText={setBirthdateMonth}
//           style={styles.dateInput}
//           placeholder="MM"
//           keyboardType="numeric"
//         />

//         <TextInput
//           label="DD"
//           value={birthdateDay}
//           onChangeText={setBirthdateDay}
//           style={styles.dateInput}
//           placeholder="DD"
//           keyboardType="numeric"
//         />
//       </View>

//       <TextInput
//         label="Gender"
//         value={gender}
//         onChangeText={setGender}
//         style={styles.input}
//       />

//       <Button mode="contained" onPress={handleNext} style={styles.button}>
//         Next
//       </Button>
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     padding: 16,
//     justifyContent: 'center',
//   },
//   input: {
//     marginBottom: 16,
//   },
//   phoneInput: {
//     fontSize: 16,
//     paddingHorizontal: 16,
//   },
//   button: {
//     marginTop: 16,
//   },
//   image: {
//     width: 200,
//     height: 200,
//     marginBottom: 16,
//   },
//   dateContainer: {
//     flexDirection: 'row',
//     marginBottom: 16,
//   },
//   dateInput: {
//     flex: 1,
//     marginRight: 8,
//   },
// });

// export default PersonalInfoScreen;
