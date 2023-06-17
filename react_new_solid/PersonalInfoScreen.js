import React, { useState, useContext, useEffect } from 'react';
import { View, StyleSheet, Image, ScrollView } from 'react-native';
import { TextInput, Button, Text } from 'react-native-paper';
import PhoneInput from 'react-native-phone-input';
import * as ImagePicker from 'expo-image-picker';
import UploadPhoto from './UploadPhoto';
import { MaterialIcons } from '@expo/vector-icons';
import { Picker } from '@react-native-picker/picker';
import { CsrfTokenContext } from "./CsrfTokenContext";
import axios from "axios"
import DateTimePicker from '@react-native-community/datetimepicker';

async function getCsrfToken() {
  const loginResponse = await axios.get('http://10.100.102.11:8000/user/get-csrf-token/');
  const csrfTokenHeader = loginResponse.headers['set-cookie']
    .find(cookie => cookie.startsWith('csrftoken'));
  if (csrfTokenHeader) {
    const csrfToken = csrfTokenHeader.split('=')[1].split(';')[0];
    return csrfToken;
  }
}

const genderOptions = [
  { label: 'Female', value: 'F' },
  { label: 'Male', value: 'M' },
  { label: 'Not Defined', value: 'N' },
];

const occupationOptions = [
  { label: 'Full-time job', value: 'F' },
  { label: 'Part-time job', value: 'P' },
  { label: 'Student', value: 'S' },
  { label: 'Doesn\'t matter', value: 'D' },
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
  { label: 'Doesn\'t matter', value: 'D' },
];

const hospitalityOptions = [
  { label: 'Love', value: 'L' },
  { label: 'Prefer Not', value: 'N' },
];

const kosherOptions = [
  { label: 'Yes', value: 'Y' },
  { label: 'No', value: 'N' },
];

const expenseManagementOptions = [
  { label: 'Prefer', value: 'L' },
  { label: 'Prefer Not', value: 'P' },
];


const PersonalInfoScreen = ({ navigation }) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [birthdateYear, setBirthdateYear] = useState('');
  const [birthdateMonth, setBirthdateMonth] = useState('');
  const [birthdateDay, setBirthdateDay] = useState('');
  const [birthdate, setBirthdate] = useState(new Date());
  const [gender, setGender] = useState('');
  const [selectedImage, setSelectedImage] = useState(require('./assets/default_for_profile.jpg'));

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

  const [firstNameError, setFirstNameError] = useState(undefined);
  const [lastNameError, setLastNameError] = useState(undefined);
  const [phoneNumberError, setPhoneNumberError] = useState(undefined);
  const [birthdateError, setBirthdateError] = useState(undefined);
  const [genderError, setGenderError] = useState(undefined);
  const [selectedImageError, setSelectedImageError] = useState(undefined);
  const [aboutMeError, setAboutMeError] = useState(undefined);
  const [occupationError, setOccupationError] = useState(undefined);
  const [smokerError, setSmokerError] = useState(undefined);
  const [dietError, setDietError] = useState(undefined);
  const [statusError, setStatusError] = useState(undefined);
  const [hospitalityError, setHospitalityError] = useState(undefined);
  const [kosherError, setKosherError] = useState(undefined);
  const [expenseManagementError, setExpenseManagementError] = useState(undefined);

  useEffect(()=>{
    console.log(birthdate);
  }, [birthdate])

  const csrfToken = useContext(CsrfTokenContext);

  const server_url = "http://10.100.102.11:8000/user/fill_info/noale/";


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

  const handleNext = async () => {
    const formData = new FormData();
    formData.append('first_name', firstName);
    formData.append('last_name', lastName);
    formData.append('phone_number', phoneNumber);
    formData.append('birthdate', birthdate.toISOString().split('T')[0]);
    formData.append('gender', gender);
    formData.append('selectedImage', selectedImage);
    formData.append('aboutMe', aboutMe);
    formData.append('occupation', occupation);
    formData.append('smoker', smoker);
    formData.append('diet', diet);
    formData.append('status', status);
    formData.append('hospitality', hospitality);
    formData.append('kosher', kosher);
    formData.append('expenseManagement', expenseManagement);

    await axios.post(server_url, formData, {
      headers: {
        'X-CSRFToken': await getCsrfToken(),
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        console.log(response.data);
        console.log('Sign up successful');
        navigation.navigate('Selection');
      })
      .catch((error) => {
        console.log("error: ", error.response.data.errors);
        const errors = JSON.parse(error.response.data.errors);

        if (errors.first_name == undefined)
          setFirstNameError(undefined);
        else
          setFirstNameError(errors.first_name[0].message);

        if (errors.last_name == undefined)
          setLastNameError(undefined);
        else
          setLastNameError(errors.last_name[0].message);

        if (errors.phone_number == undefined)
          setPhoneNumberError(undefined);
        else
          setPhoneNumberError(errors.phone_number[0].message);

        if (errors.birthdate == undefined)
          setBirthdateError(undefined);
        else
          setBirthdateError(errors.birthdate[0].message);

        if (errors.gender == undefined)
          setGenderError(undefined);
        else
          setGenderError(errors.gender[0].message);

        if (errors.selectedImage == undefined)
          setSelectedImageError(undefined);
        else
          setSelectedImageError(errors.selectedImage[0].message);

        if (errors.aboutMe == undefined)
          setAboutMeError(undefined);
        else
          setAboutMeError(errors.aboutMe[0].message);

        if (errors.occupation == undefined)
          setOccupationError(undefined);
        else
          setOccupationError(errors.occupation[0].message);

        if (errors.smoker == undefined)
          setSmokerError(undefined);
        else
          setSmokerError(errors.smoker[0].message);

        if (errors.diet == undefined)
          setDietError(undefined);
        else
          setDietError(errors.diet[0].message);

        if (errors.status == undefined)
          setStatusError(undefined);
        else
          setStatusError(errors.status[0].message);

        if (errors.hospitality == undefined)
          setHospitalityError(undefined);
        else
          setHospitalityError(errors.hospitality[0].message);

        if (errors.kosher == undefined)
          setKosherError(undefined);
        else
          setKosherError(errors.kosher[0].message);

        if (errors.expenseManagement == undefined)
          setExpenseManagementError(undefined);
        else
          setExpenseManagementError(errors.expenseManagement[0].message);

      }
      );
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
        {
          firstNameError && <Text style={{ color: 'red' }}>{firstNameError}</Text>
        }
        <TextInput
          label="Last Name"
          value={lastName}
          onChangeText={setLastName}
          style={styles.input}
        />
        {
          lastNameError && <Text style={{ color: 'red' }}>{lastNameError}</Text>
        }

        <PhoneInput
          initialCountry="us"
          value={phoneNumber}
          onChangePhoneNumber={setPhoneNumber}
          textStyle={styles.phoneInput}
          style={styles.input}
        />
        {
          phoneNumberError && <Text style={{ color: 'red' }}>{phoneNumberError}</Text>
        }

        <View style={styles.dateContainer}>
          <Text style={styles.label}>Birthdate:                </Text>
          <DateTimePicker
            value={birthdate}
            dateFormat='YYYY-MM-DD'
            onChange={(dateStr, date)=> {console.log(dateStr); setBirthdate(date);}}
          />

          {/* <TextInput
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
          /> */}

          {
            birthdateError && <Text style={{ color: 'red' }}>{birthdateError}</Text>
          }
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
        {
          genderError && <Text style={{ color: 'red' }}>{genderError}</Text>
        }

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
        {
          aboutMeError && <Text style={{ color: 'red' }}>{aboutMeError}</Text>
        }

        <UploadPhoto selectedImage={selectedImage} handleImageSelect={handleImageSelect} />
        {
          selectedImageError && <Text style={{ color: 'red' }}>{selectedImageError}</Text>
        }

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
        {
          occupationError && <Text style={{ color: 'red' }}>{occupationError}</Text>
        }

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
        {
          smokerError && <Text style={{ color: 'red' }}>{smokerError}</Text>
        }

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
        {
          dietError && <Text style={{ color: 'red' }}>{dietError}</Text>
        }

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
        {
          statusError && <Text style={{ color: 'red' }}>{statusError}</Text>
        }

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
        {
          hospitalityError && <Text style={{ color: 'red' }}>{hospitalityError}</Text>
        }

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
        {
          kosherError && <Text style={{ color: 'red' }}>{kosherError}</Text>
        }

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
        {
          expenseManagementError && <Text style={{ color: 'red' }}>{expenseManagementError}</Text>
        }


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
