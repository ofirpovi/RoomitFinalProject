// import React, { useState } from 'react';
// import { View, StyleSheet, Text, ScrollView } from 'react-native';
// import { Button } from 'react-native-paper';
// import { Picker } from '@react-native-picker/picker';

// const occupationOptions = [
//   { label: 'Full-time job', value: 'full-time' },
//   { label: 'Part-time job', value: 'part-time' },
//   { label: 'Student', value: 'student' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const ageOptions = [];
// for (let i = 18; i <= 40; i++) {
//   ageOptions.push({ label: String(i), value: String(i) });
// }

// const genderOptions = [
//   { label: 'Female', value: 'female' },
//   { label: 'Male', value: 'male' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const smokeOptions = [
//   { label: 'Smoke', value: 'smoke' },
//   { label: 'Not Smoke', value: 'not-smoke' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const vegetarianOptions = [
//   { label: 'Vegetarian', value: 'vegetarian' },
//   { label: 'Vegan', value: 'vegan' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const kosherOptions = [
//   { label: 'Yes', value: 'yes' },
//   { label: 'No', value: 'no' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const singleOptions = [
//   { label: 'Yes', value: 'yes' },
//   { label: 'No', value: 'no' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const IdealRoommate = () => {
//   const [occupation, setOccupation] = useState('');
//   const [minAge, setMinAge] = useState('');
//   const [maxAge, setMaxAge] = useState('');
//   const [gender, setGender] = useState('');
//   const [smoke, setSmoke] = useState('');
//   const [vegetarian, setVegetarian] = useState('');
//   const [kosher, setKosher] = useState('');
//   const [single, setSingle] = useState('');

//   const handleSubmit = () => {
//     // Handle form submission here
//   };

//   return (
//     <ScrollView style={styles.container}>
//       <Text style={styles.title}>Ideal Roommate</Text>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Occupation:</Text>
//         <Picker selectedValue={occupation} onValueChange={setOccupation}>
//           <Picker.Item label="Select occupation" value="" />
//           {occupationOptions.map((item, index) => (
//             <Picker.Item key={index} label={item.label} value={item.value} />
//           ))}
//         </Picker>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Age range:</Text>
//         <View style={styles.ageRangeContainer}>
//           <View style={styles.pickerContainer}>
//             <Text style={styles.pickerLabel}>Min</Text>
//             <Picker selectedValue={minAge} onValueChange={setMinAge}>
//               {ageOptions.map((item, index) => (
//                 <Picker.Item key={index} label={item.label} value={item.value} />
//               ))}
//             </Picker>
//           </View>
//           <View style={styles.pickerContainer}>
//             <Text style={styles.pickerLabel}>Max</Text>
//             <Picker selectedValue={maxAge} onValueChange={setMaxAge}>
//               {ageOptions.map((item, index) => (
//                 <Picker.Item key={index} label={item.label} value={item.value} />
//               ))}
//             </Picker>
//           </View>
//         </View>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Gender:</Text>
//         <Picker selectedValue={gender} onValueChange={setGender}>
//           <Picker.Item label="Select gender" value="" />
//           {genderOptions.map((item, index) => (
//             <Picker.Item key={index} label={item.label} value={item.value} />
//           ))}
//         </Picker>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Smoke:</Text>
//         <Picker selectedValue={smoke} onValueChange={setSmoke}>
//           <Picker.Item label="Select smoke preference" value="" />
//           {smokeOptions.map((item, index) => (
//             <Picker.Item key={index} label={item.label} value={item.value} />
//           ))}
//         </Picker>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Vegetarianism/veganism:</Text>
//         <Picker selectedValue={vegetarian} onValueChange={setVegetarian}>
//           <Picker.Item label="Select dietary preference" value="" />
//           {vegetarianOptions.map((item, index) => (
//             <Picker.Item key={index} label={item.label} value={item.value} />
//           ))}
//         </Picker>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Kosher:</Text>
//         <Picker selectedValue={kosher} onValueChange={setKosher}>
//           <Picker.Item label="Select kosher preference" value="" />
//           {kosherOptions.map((item, index) => (
//             <Picker.Item key={index} label={item.label} value={item.value} />
//           ))}
//         </Picker>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Single:</Text>
//         <Picker selectedValue={single} onValueChange={setSingle}>
//           <Picker.Item label="Select single status" value="" />
//           {singleOptions.map((item, index) => (
//             <Picker.Item key={index} label={item.label} value={item.value} />
//           ))}
//         </Picker>
//       </View>

//       <Button mode="contained" onPress={handleSubmit} style={styles.submitButton}>
//         Submit
//       </Button>
//     </ScrollView>
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
//     marginBottom: 20,
//   },
//   fieldContainer: {
//     marginBottom: 16,
//   },
//   label: {
//     fontSize: 14,
//     marginBottom: 8,
//   },
//   ageRangeContainer: {
//     flexDirection: 'row',
//     justifyContent: 'space-between',
//   },
//   pickerContainer: {
//     flex: 1,
//   },
//   pickerLabel: {
//     fontSize: 12,
//     marginBottom: 4,
//   },
//   submitButton: {
//     marginTop: 16,
//   },
// });

// export default IdealRoommate;





import React, { useState } from 'react';
import { View, StyleSheet, Text, ScrollView } from 'react-native';
import { Button } from 'react-native-paper';
import { Picker } from '@react-native-picker/picker';
import { useNavigation } from '@react-navigation/native';

const occupationOptions = [
  { label: 'Full-time job', value: 'full-time' },
  { label: 'Part-time job', value: 'part-time' },
  { label: 'Student', value: 'student' },
  { label: 'Not Important', value: 'not-important' },
];

const ageOptions = [];
for (let i = 18; i <= 40; i++) {
  ageOptions.push({ label: String(i), value: String(i) });
}

const genderOptions = [
  { label: 'Female', value: 'female' },
  { label: 'Male', value: 'male' },
  { label: 'Not Important', value: 'not-important' },
];

const smokeOptions = [
  { label: 'Smoke', value: 'smoke' },
  { label: 'Not Smoke', value: 'not-smoke' },
  { label: 'Not Important', value: 'not-important' },
];

const vegetarianOptions = [
  { label: 'Vegetarian', value: 'vegetarian' },
  { label: 'Vegan', value: 'vegan' },
  { label: 'Not Important', value: 'not-important' },
];

const kosherOptions = [
  { label: 'Yes', value: 'yes' },
  { label: 'No', value: 'no' },
  { label: 'Not Important', value: 'not-important' },
];

const singleOptions = [
  { label: 'Yes', value: 'yes' },
  { label: 'No', value: 'no' },
  { label: 'Not Important', value: 'not-important' },
];

const IdealRoommate = () => {
  const [occupation, setOccupation] = useState('');
  const [minAge, setMinAge] = useState('');
  const [maxAge, setMaxAge] = useState('');
  const [gender, setGender] = useState('');
  const [smoke, setSmoke] = useState('');
  const [vegetarian, setVegetarian] = useState('');
  const [kosher, setKosher] = useState('');
  const [single, setSingle] = useState('');
  const navigation = useNavigation();

  const handleSubmit = () => {
    navigation.navigate('RegistrationSuccess');
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
      </View>

      <View style={styles.fieldContainer}>
        <Text style={styles.label}>Smoke:</Text>
        <View style={[styles.picker, smoke && styles.pickerSelected]}>
          <Picker selectedValue={smoke} onValueChange={setSmoke}>
            <Picker.Item label="Select smoke preference" value="" />
            {smokeOptions.map((item, index) => (
              <Picker.Item key={index} label={item.label} value={item.value} />
            ))}
          </Picker>
        </View>
      </View>

      <View style={styles.fieldContainer}>
        <Text style={styles.label}>Vegetarianism/veganism:</Text>
        <View style={[styles.picker, vegetarian && styles.pickerSelected]}>
          <Picker selectedValue={vegetarian} onValueChange={setVegetarian}>
            <Picker.Item label="Select dietary preference" value="" />
            {vegetarianOptions.map((item, index) => (
              <Picker.Item key={index} label={item.label} value={item.value} />
            ))}
          </Picker>
        </View>
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
      </View>

      <View style={styles.fieldContainer}>
        <Text style={styles.label}>Single:</Text>
        <View style={[styles.picker, single && styles.pickerSelected]}>
          <Picker selectedValue={single} onValueChange={setSingle}>
            <Picker.Item label="Select single status" value="" />
            {singleOptions.map((item, index) => (
              <Picker.Item key={index} label={item.label} value={item.value} />
            ))}
          </Picker>
        </View>
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



// import React, { useState } from 'react';
// import { View, StyleSheet, Text, ScrollView } from 'react-native';
// import { Button } from 'react-native-paper';
// import { Picker } from '@react-native-picker/picker';
// import { useNavigation } from '@react-navigation/native';

// const occupationOptions = [
//   { label: 'Full-time job', value: 'full-time' },
//   { label: 'Part-time job', value: 'part-time' },
//   { label: 'Student', value: 'student' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const ageOptions = [];
// for (let i = 18; i <= 40; i++) {
//   ageOptions.push({ label: String(i), value: String(i) });
// }

// const genderOptions = [
//   { label: 'Female', value: 'female' },
//   { label: 'Male', value: 'male' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const smokeOptions = [
//   { label: 'Smoke', value: 'smoke' },
//   { label: 'Not Smoke', value: 'not-smoke' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const vegetarianOptions = [
//   { label: 'Vegetarian', value: 'vegetarian' },
//   { label: 'Vegan', value: 'vegan' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const kosherOptions = [
//   { label: 'Yes', value: 'yes' },
//   { label: 'No', value: 'no' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const singleOptions = [
//   { label: 'Yes', value: 'yes' },
//   { label: 'No', value: 'no' },
//   { label: 'Not Important', value: 'not-important' },
// ];

// const IdealRoommate = () => {
//   const [occupation, setOccupation] = useState('');
//   const [minAge, setMinAge] = useState('');
//   const [maxAge, setMaxAge] = useState('');
//   const [gender, setGender] = useState('');
//   const [smoke, setSmoke] = useState('');
//   const [vegetarian, setVegetarian] = useState('');
//   const [kosher, setKosher] = useState('');
//   const [single, setSingle] = useState('');
//   const navigation = useNavigation();

//   const handleSubmit = () => {
//     navigation.navigate('RegistrationSuccess');
//   };

//   return (
//     <ScrollView style={styles.container}>
//       <Text style={styles.title}>Ideal Roommate</Text>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Occupation:</Text>
//         <View style={[styles.picker, occupation && styles.pickerSelected]}>
//           <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={occupation} onValueChange={setOccupation}>
//             <Picker.Item label="Select occupation" value="" />
//             {occupationOptions.map((item, index) => (
//               <Picker.Item key={index} label={item.label} value={item.value} />
//             ))}
//           </Picker>
//         </View>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Age range:</Text>
//         <View style={styles.ageRangeContainer}>
//           <View style={styles.pickerContainer}>
//             <Text style={styles.pickerLabel}>Min</Text>
//             <View style={[styles.picker, minAge && styles.pickerSelected]}>
//               <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={minAge} onValueChange={setMinAge}>
//                 {ageOptions.map((item, index) => (
//                   <Picker.Item key={index} label={item.label} value={item.value} />
//                 ))}
//               </Picker>
//             </View>
//           </View>
//           <View style={styles.pickerContainer}>
//             <Text style={styles.pickerLabel}>Max</Text>
//             <View style={[styles.picker, maxAge && styles.pickerSelected]}>
//               <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={maxAge} onValueChange={setMaxAge}>
//                 {ageOptions.map((item, index) => (
//                   <Picker.Item key={index} label={item.label} value={item.value} />
//                 ))}
//               </Picker>
//             </View>
//           </View>
//         </View>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Gender:</Text>
//         <View style={[styles.picker, gender && styles.pickerSelected]}>
//           <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={gender} onValueChange={setGender}>
//             <Picker.Item label="Select gender" value="" />
//             {genderOptions.map((item, index) => (
//               <Picker.Item key={index} label={item.label} value={item.value} />
//             ))}
//           </Picker>
//         </View>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Smoke:</Text>
//         <View style={[styles.picker, smoke && styles.pickerSelected]}>
//           <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={smoke} onValueChange={setSmoke}>
//             <Picker.Item label="Select smoke preference" value="" />
//             {smokeOptions.map((item, index) => (
//               <Picker.Item key={index} label={item.label} value={item.value} />
//             ))}
//           </Picker>
//         </View>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Vegetarianism/veganism:</Text>
//         <View style={[styles.picker, vegetarian && styles.pickerSelected]}>
//           <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={vegetarian} onValueChange={setVegetarian}>
//             <Picker.Item label="Select dietary preference" value="" />
//             {vegetarianOptions.map((item, index) => (
//               <Picker.Item key={index} label={item.label} value={item.value} />
//             ))}
//           </Picker>
//         </View>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Kosher:</Text>
//         <View style={[styles.picker, kosher && styles.pickerSelected]}>
//           <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={kosher} onValueChange={setKosher}>
//             <Picker.Item label="Select kosher preference" value="" />
//             {kosherOptions.map((item, index) => (
//               <Picker.Item key={index} label={item.label} value={item.value} />
//             ))}
//           </Picker>
//         </View>
//       </View>

//       <View style={styles.fieldContainer}>
//         <Text style={styles.label}>Single:</Text>
//         <View style={[styles.picker, single && styles.pickerSelected]}>
//           <Picker style={styles.picker} itemStyle={styles.pickerItem} selectedValue={single} onValueChange={setSingle}>
//             <Picker.Item label="Select single status" value="" />
//             {singleOptions.map((item, index) => (
//               <Picker.Item key={index} label={item.label} value={item.value} />
//             ))}
//           </Picker>
//         </View>
//       </View>

//       <Button mode="contained" onPress={handleSubmit} style={styles.submitButton}>
//         Save and create my profile!
//       </Button>
//       <View style={{ height: 70 }}></View>
//     </ScrollView>
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
//     marginBottom: 20,
//   },
//   fieldContainer: {
//     marginBottom: 16,
//   },
//   label: {
//     fontSize: 14,
//     marginBottom: 8,
//   },
//   ageRangeContainer: {
//     flexDirection: 'row',
//     justifyContent: 'space-between',
//   },
//   pickerContainer: {
//     flex: 1,
//   },
//   pickerLabel: {
//     fontSize: 12,
//     marginBottom: 4,
//   },
//   picker: {
//     backgroundColor: '#FFFFFF',
//     borderRadius: 4,
//     borderWidth: 1,
//     borderColor: '#CCCCCC',
//     padding: 8,
//   },
//   pickerSelected: {
//     backgroundColor: '#EBE2EF',
//   },
//   submitButton: {
//     marginTop: 16,
//   },
//   pickerItem: {
//     fontSize: 18,
//   },
// });

// export default IdealRoommate;
