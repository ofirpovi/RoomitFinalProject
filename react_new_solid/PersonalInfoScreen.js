import React, { useState } from 'react';
import { View, StyleSheet, Image, ScrollView } from 'react-native';
import { TextInput, Button, Text } from 'react-native-paper';
import PhoneInput from 'react-native-phone-input';
import * as ImagePicker from 'expo-image-picker';
import UploadPhoto from './UploadPhoto';
import { MaterialIcons } from '@expo/vector-icons';
import { Picker } from '@react-native-picker/picker';

const genderOptions = [
  { label: 'Female', value: 'Female' },
  { label: 'Male', value: 'Male' },
  { label: 'Not Defined', value: 'Not Defined' },
];

const occupationOptions = [
  { label: 'Full-time job', value: 'Full-time job' },
  { label: 'Part-time job', value: 'Part-time job' },
  { label: 'Student', value: 'Student' },
  { label: 'Doesn\'t matter', value: 'Doesn\'t matter' },
];

const smokerOptions = [
  { label: 'Yes', value: 'Yes' },
  { label: 'No', value: 'No' },
  { label: 'Occassionally', value: 'Occassionally' },
  { label: 'Socially', value: 'Socially' },
];

const dietOptions = [
  { label: 'Carnivore', value: 'Carnivore' },
  { label: 'Pescetarian', value: 'Pescetarian' },
  { label: 'Vegetarian', value: 'Vegetarian' },
  { label: 'Vegan', value: 'Vegan' },
  { label: 'Raw Veganism', value: 'Raw Veganism' },
];

const statusOptions = [
  { label: 'Single', value: 'Single' },
  { label: 'Married', value: 'Married' },
  { label: 'In a relationship', value: 'In a relationship' },
  { label: 'Doesn\'t matter', value: 'Doesn\'t matter' },
];

const hospitalityOptions = [
  { label: 'Love', value: 'Love' },
  { label: 'Prefer Not', value: 'Prefer Not' },
];

const kosherOptions = [
  { label: 'Yes', value: 'Yes' },
  { label: 'No', value: 'No' },
];

const expenseManagementOptions = [
  { label: 'Prefer', value: 'Prefer' },
  { label: 'Prefer Not', value: 'Prefer Not' },
];


const PersonalInfoScreen = ({ navigation }) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [birthdateYear, setBirthdateYear] = useState('');
  const [birthdateMonth, setBirthdateMonth] = useState('');
  const [birthdateDay, setBirthdateDay] = useState('');
  const [gender, setGender] = useState('');
  const [selectedImage, setSelectedImage] = useState(require('./assets/default_for_profile.jpg'));
  // const [occupation, setOccupation] = useState(''); // 'Yes' or 'No'
  // const [smoking, setSmoking] = useState(''); // 'Yes' or 'No'
  // const [diet, setDiet] = useState(''); // 'Yes' or 'No'
  // const [kosher, setKosher] = useState(''); // 'Yes' or 'No'
  // const [single, setSingle] = useState(''); // 'Yes' or 'No'
  // const [hospitality, setHospitality] = useState(''); // 'Yes' or 'No'
  // const [sharingShopping, setSharingShopping] = useState(''); // 'Yes' or 'No'
  const [isFontLoaded, setIsFontLoaded] = useState(false);
  const [selection, setSelection] = useState('');
  const [aboutMe, setAboutMe] = useState('');

  const [occupation, setOccupation] = useState('');
  const [smoker, setSmoker] = useState('');
  const [diet, setDiet] = useState('');
  const [status, setStatus] = useState('');
  const [hospitality, setHospitality] = useState('');
  const [kosher, setKosher] = useState('');
  const [expenseManagement, setExpenseManagement] = useState('');




  const handleImageSelect = async () => {
    const permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync();

    if (permissionResult.granted === false) {
      alert('Permission to access the camera roll is required!');
      return;
    }

    const result = await ImagePicker.launchImageLibraryAsync();

    if (!result.cancelled) {
      setSelectedImage({ uri: result.uri });
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
    navigation.navigate('Selection');
  };

  return (
    <View style={styles.container}>
      <ScrollView>
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

        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Gender:</Text>
          <View style={[styles.picker, gender && styles.pickerSelected]}>
            <Picker selectedValue={gender} onValueChange={setGender}>
              <Picker.Item label="Select gender" value="" />
              {genderOptions.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>
        </View>

        <View style={styles.rowContainer}>
          <Text style={styles.label}>About Me:</Text>
          <TextInput
            multiline
            numberOfLines={6}
            value={aboutMe}
            onChangeText={setAboutMe}
            style={[styles.input, { height: 120, textAlignVertical: 'top' }]}
          />
        </View>

        <UploadPhoto selectedImage={selectedImage} handleImageSelect={handleImageSelect} />


        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Occupation:</Text>
          <View style={[styles.picker, occupation && styles.pickerSelected]}>
            <Picker selectedValue={occupation} onValueChange={setOccupation}>
              <Picker.Item label="Select occupation" value="" />
              {occupationOptions.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>
        </View>

        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Smoker:</Text>
          <View style={[styles.picker, smoker && styles.pickerSelected]}>
            <Picker selectedValue={smoker} onValueChange={setSmoker}>
              <Picker.Item label="Select smoker" value="" />
              {smokerOptions.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>
        </View>

        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Diet:</Text>
          <View style={[styles.picker, diet && styles.pickerSelected]}>
            <Picker selectedValue={diet} onValueChange={setDiet}>
              <Picker.Item label="Select diet" value="" />
              {dietOptions.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>
        </View>

        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Status:</Text>
          <View style={[styles.picker, status && styles.pickerSelected]}>
            <Picker selectedValue={status} onValueChange={setStatus}>
              <Picker.Item label="Select status" value="" />
              {statusOptions.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>
        </View>

        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Hospitality:</Text>
          <View style={[styles.picker, hospitality && styles.pickerSelected]}>
            <Picker selectedValue={hospitality} onValueChange={setHospitality}>
              <Picker.Item label="Select hospitality" value="" />
              {hospitalityOptions.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>
        </View>

        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Kosher:</Text>
          <View style={[styles.picker, kosher && styles.pickerSelected]}>
            <Picker selectedValue={kosher} onValueChange={setKosher}>
              <Picker.Item label="Select kosher" value="" />
              {kosherOptions.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>
        </View>

        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Expense Management:</Text>
          <View style={[styles.picker, expenseManagement && styles.pickerSelected]}>
            <Picker selectedValue={expenseManagement} onValueChange={setExpenseManagement}>
              <Picker.Item label="Select expense management" value="" />
              {expenseManagementOptions.map((item, index) => (
                <Picker.Item key={index} label={item.label} value={item.value} />
              ))}
            </Picker>
          </View>
        </View>


      </ScrollView>
      <Button mode="contained" onPress={handleNext} style={styles.button}>
        Next
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    justifyContent: 'center',
  },
  additionalInfoContainer: {
    justifyContent: 'center',
  },
  photoContainer: {
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
  additionalInfoInput: {
    marginBottom: 16,
    flex: 1,
  },
  phoneInput: {
    fontSize: 16,
    paddingHorizontal: 16,
  },
  button: {
    marginTop: 16,
  },
  option: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  icon: {
    marginRight: 16,
  },
  label: {
    fontSize: 14,
    marginRight: 8,
  },
  image: {
    width: 200,
    height: 200,
    marginBottom: 16,
  },
  fieldContainer: {
    marginBottom: 16,
  },
  pickerContainer: {
    flex: 1,
  },
  pickerLabel: {
    fontSize: 12,
    marginBottom: 4,
  },
  picker: {
    backgroundColor: '#FFFFFF',
    borderRadius: 4,
    borderWidth: 1,
    borderColor: '#CCCCCC',
    padding: 8,
  },
  pickerSelected: {
    backgroundColor: '#EBE2EF',
  },
});

export default PersonalInfoScreen;
