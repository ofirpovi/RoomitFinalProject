import React, { useState } from 'react';
import { View, StyleSheet, Text, ScrollView } from 'react-native';
import { Button } from 'react-native-paper';
import { Picker } from '@react-native-picker/picker';
import { useNavigation } from '@react-navigation/native';
import axios from "axios";
import { tokenGenerator } from "./tokenGenerator";

const occupationOptions = [
  { label: 'Full-time job', value: 'F' },
  { label: 'Part-time job', value: 'P' },
  { label: 'Student', value: 'S' },
  { label: 'Doesn\'t matter', value: 'D' },
];

const ageOptions = [];
for (let i = 18; i <= 40; i++) {
  ageOptions.push({ label: String(i), value: String(i) });
}

const genderOptions = [
  { label: 'Female', value: 'F' },
  { label: 'Male', value: 'M' },
  { label: 'Not Defined', value: 'N' },
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

const kosherOptions = [
  { label: 'Yes', value: 'Y' },
  { label: 'No', value: 'N' },
];

const statusOptions = [
  { label: 'Single', value: 'Single' },
  { label: 'Married', value: 'Married' },
  { label: 'In a relationship', value: 'In a relationship' },
  { label: 'Doesn\'t matter', value: 'D' },
];

const expenseManagementOptions = [
  { label: 'Prefer', value: 'L' },
  { label: 'Prefer Not', value: 'P' },
];

const hospitalityOptions = [
  { label: 'Love', value: 'L' },
  { label: 'Prefer Not', value: 'N' },
];


const IdealRoommate = ({ navigation, route }) => {
  console.log("IdealRoomate");
  console.log(route.params.username);
  username = route.params.username;
  const [occupation, setOccupation] = useState('');
  const [minAge, setMinAge] = useState('');
  const [maxAge, setMaxAge] = useState('');
  const [gender, setGender] = useState('');
  const [smoker, setSmoker] = useState('');
  const [diet, setDiet] = useState('');
  const [kosher, setKosher] = useState('');
  const [status, setStatus] = useState('');
  const [expenseManagement, setExpenseManagement] = useState('');
  const [hospitality, setHospitality] = useState('');
  // const navigation = useNavigation();
  const [occupationError, setOccupationError] = useState(undefined);
  const [genderError, setGenderError] = useState(undefined);
  const [smokerError, setSmokerError] = useState(undefined);
  const [dietError, setDietError] = useState(undefined);
  const [kosherError, setKosherError] = useState(undefined);
  const [statusError, setStatusError] = useState(undefined);
  const [expenseManagementError, setExpenseManagementError] = useState(undefined);
  const [hospitalityError, setHospitalityError] = useState(undefined);

  const server_url = `http://192.168.1.171:8000/requirementsR/${username}/`;



  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('occupation', occupation);
    formData.append('minAge', minAge);
    formData.append('maxAge', maxAge);
    formData.append('gender', gender);
    formData.append('smoker', smoker);
    formData.append('diet', diet);
    formData.append('kosher', kosher);
    formData.append('status', status);
    formData.append('Expense_Management', expenseManagement);
    formData.append('Hospitality', hospitality);

    await axios.post(server_url, formData, {
      headers: {
        'X-CSRFToken': await tokenGenerator.getCsrfToken(),
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        console.log(response.data);
        navigation.navigate('RegistrationSuccess', { username: username });
      })
      .catch((error) => {
        console.log("error: ", error.response.data.errors);
        const errors = JSON.parse(error.response.data.errors);
        if (errors.occupation == undefined)
          setOccupationError(undefined);
        else
          setOccupationError(errors.occupation[0].message);

        if (errors.gender == undefined)
          setGenderError(undefined);
        else
          setGenderError(errors.gender[0].message);

        if (errors.smoker == undefined)
          setSmokerError(undefined);
        else
          setSmokerError(errors.smoker[0].message);

        if (errors.diet == undefined)
          setDietError(undefined);
        else
          setDietError(errors.diet[0].message);

        if (errors.kosher == undefined)
          setKosherError(undefined);
        else
          setKosherError(errors.kosher[0].message);

        if (errors.status == undefined)
          setStatusError(undefined);
        else
          setStatusError(errors.status[0].message);

        if (errors.expenseManagement == undefined)
          setExpenseManagementError(undefined);
        else
          setExpenseManagementError(errors.expenseManagement[0].message);

        if (errors.hospitality == undefined)
          setHospitalityError(undefined);
        else
          setHospitalityError(errors.hospitality[0].message);
      }
      );

  };

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Ideal Roommate</Text>

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
        {
          occupationError && <Text style={{ color: 'red' }}>{occupationError}</Text>
        }
      </View>

      <View style={styles.fieldContainer}>
        <Text style={styles.label}>Age range:</Text>
        <View style={styles.ageRangeContainer}>
          <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Min</Text>
            <View style={[styles.picker, minAge && styles.pickerSelected]}>
              <Picker selectedValue={minAge} onValueChange={setMinAge}>
                {ageOptions.map((item, index) => (
                  <Picker.Item key={index} label={item.label} value={item.value} />
                ))}
              </Picker>
            </View>
          </View>
          <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Max</Text>
            <View style={[styles.picker, maxAge && styles.pickerSelected]}>
              <Picker selectedValue={maxAge} onValueChange={setMaxAge}>
                {ageOptions.map((item, index) => (
                  <Picker.Item key={index} label={item.label} value={item.value} />
                ))}
              </Picker>
            </View>
          </View>
        </View>
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
        {
          genderError && <Text style={{ color: 'red' }}>{genderError}</Text>
        }
      </View>

      <View style={styles.fieldContainer}>
        <Text style={styles.label}>Smoker:</Text>
        <View style={[styles.picker, smoker && styles.pickerSelected]}>
          <Picker selectedValue={smoker} onValueChange={setSmoker}>
            <Picker.Item label="Select smoker preference" value="" />
            {smokerOptions.map((item, index) => (
              <Picker.Item key={index} label={item.label} value={item.value} />
            ))}
          </Picker>
        </View>
        {
          smokerError && <Text style={{ color: 'red' }}>{smokerError}</Text>
        }
      </View>

      <View style={styles.fieldContainer}>
        <Text style={styles.label}>Diet:</Text>
        <View style={[styles.picker, diet && styles.pickerSelected]}>
          <Picker selectedValue={diet} onValueChange={setDiet}>
            <Picker.Item label="Select dietary preference" value="" />
            {dietOptions.map((item, index) => (
              <Picker.Item key={index} label={item.label} value={item.value} />
            ))}
          </Picker>
        </View>
        {
          dietError && <Text style={{ color: 'red' }}>{dietError}</Text>
        }
      </View>

      <View style={styles.fieldContainer}>
        <Text style={styles.label}>Kosher:</Text>
        <View style={[styles.picker, kosher && styles.pickerSelected]}>
          <Picker selectedValue={kosher} onValueChange={setKosher}>
            <Picker.Item label="Select kosher preference" value="" />
            {kosherOptions.map((item, index) => (
              <Picker.Item key={index} label={item.label} value={item.value} />
            ))}
          </Picker>
        </View>
        {
          kosherError && <Text style={{ color: 'red' }}>{kosherError}</Text>
        }
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
        {
          statusError && <Text style={{ color: 'red' }}>{statusError}</Text>
        }
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
      {
        expenseManagementError && <Text style={{ color: 'red' }}>{expenseManagementError}</Text>
      }
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
        {
          hospitalityError && <Text style={{ color: 'red' }}>{hospitalityError}</Text>
        }
      </View>

      <Button mode="contained" onPress={handleSubmit} style={styles.submitButton}>
        Save and create my profile!
      </Button>
      <View style={{ height: 70 }}></View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  fieldContainer: {
    marginBottom: 16,
  },
  label: {
    fontSize: 14,
    marginBottom: 8,
  },
  ageRangeContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
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
  submitButton: {
    marginTop: 16,
  },
});

export default IdealRoommate;
