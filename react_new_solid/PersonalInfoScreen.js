import React, { useState } from 'react';
import { View, StyleSheet, Image, ScrollView } from 'react-native';
import { TextInput, Button, Text } from 'react-native-paper';
import PhoneInput from 'react-native-phone-input';
import * as ImagePicker from 'expo-image-picker';
import UploadPhoto from './UploadPhoto';
import { MaterialIcons } from '@expo/vector-icons';


const PersonalInfoScreen = ({ navigation }) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [birthdateYear, setBirthdateYear] = useState('');
  const [birthdateMonth, setBirthdateMonth] = useState('');
  const [birthdateDay, setBirthdateDay] = useState('');
  const [gender, setGender] = useState('');
  const [selectedImage, setSelectedImage] = useState(require('./assets/default_for_profile.jpg'));
  const [occupation, setOccupation] = useState(''); // 'Yes' or 'No'
  const [smoking, setSmoking] = useState(''); // 'Yes' or 'No'
  const [diet, setDiet] = useState(''); // 'Yes' or 'No'
  const [kosher, setKosher] = useState(''); // 'Yes' or 'No'
  const [single, setSingle] = useState(''); // 'Yes' or 'No'
  const [hospitality, setHospitality] = useState(''); // 'Yes' or 'No'
  const [sharingShopping, setSharingShopping] = useState(''); // 'Yes' or 'No'
  const [isFontLoaded, setIsFontLoaded] = useState(false);
  const [selection, setSelection] = useState('');

  const handleImageSelect = async () => {
    const permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync();

    if (permissionResult.granted === false) {
      alert('Permission to access the camera roll is required!');
      return;
    }

    const result = await ImagePicker.launchImageLibraryAsync();

    if (!result.cancelled) {
      setSelectedImage({uri: result.uri});
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

        <TextInput
          label="Gender"
          value={gender}
          onChangeText={setGender}
          style={styles.input}
        />

        <UploadPhoto selectedImage={selectedImage} handleImageSelect={handleImageSelect} />

        <View style={styles.additionalInfoContainer}>
          <View style={styles.option}>
            <MaterialIcons
              name={occupation === 'Yes' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setOccupation('Yes')}
              style={styles.icon}
            />
            <MaterialIcons
              name={occupation === 'No' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setOccupation('No')}
              style={styles.icon}
            />
            <TextInput
              label="Occupation"
              value={occupation}
              style={styles.additionalInfoInput}
              editable={false}
            />
          </View>

          <View style={styles.option}>
            <MaterialIcons
              name={smoking === 'Yes' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setSmoking('Yes')}
              style={styles.icon}
            />
            <MaterialIcons
              name={smoking === 'No' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setSmoking('No')}
              style={styles.icon}
            />
            <TextInput
              label="Smoking"
              value={smoking}
              style={styles.additionalInfoInput}
              editable={false}
            />
          </View>

          <View style={styles.option}>
            <MaterialIcons
              name={diet === 'Yes' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setDiet('Yes')}
              style={styles.icon}
            />
            <MaterialIcons
              name={diet === 'No' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setDiet('No')}
              style={styles.icon}
            />
            <TextInput
              label="Diet"
              value={diet}
              style={styles.additionalInfoInput}
              editable={false}
            />
          </View>

          <View style={styles.option}>
            <MaterialIcons
              name={kosher === 'Yes' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setKosher('Yes')}
              style={styles.icon}
            />
            <MaterialIcons
              name={kosher === 'No' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setKosher('No')}
              style={styles.icon}
            />
            <TextInput
              label="Kosher"
              value={kosher}
              style={styles.additionalInfoInput}
              editable={false}
            />
          </View>

          <View style={styles.option}>
            <MaterialIcons
              name={single === 'Yes' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setSingle('Yes')}
              style={styles.icon}
            />
            <MaterialIcons
              name={single === 'No' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setSingle('No')}
              style={styles.icon}
            />
            <TextInput
              label="Single"
              value={single}
              style={styles.additionalInfoInput}
              editable={false}
            />
          </View>

          <View style={styles.option}>
            <MaterialIcons
              name={hospitality === 'Yes' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setHospitality('Yes')}
              style={styles.icon}
            />
            <MaterialIcons
              name={hospitality === 'No' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setHospitality('No')}
              style={styles.icon}
            />
            <TextInput
              label="Hospitality"
              value={hospitality}
              style={styles.additionalInfoInput}
              editable={false}
            />
          </View>

          <View style={styles.option}>
            <MaterialIcons
              name={sharingShopping === 'Yes' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setSharingShopping('Yes')}
              style={styles.icon}
            />
            <MaterialIcons
              name={sharingShopping === 'No' ? 'check-box' : 'check-box-outline-blank'}
              size={24}
              color="black"
              onPress={() => setSharingShopping('No')}
              style={styles.icon}
            />
            <TextInput
              label="Sharing Shopping"
              value={sharingShopping}
              style={styles.additionalInfoInput}
              editable={false}
            />
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
    fontSize: 16,
    marginRight: 8,
  },
  image: {
    width: 200,
    height: 200,
    marginBottom: 16,
  },
});

export default PersonalInfoScreen;
