import React, { useState, useContext } from 'react';
import { View, StyleSheet, Text, TextInput, ScrollView, Image, KeyboardAvoidingView } from 'react-native';
import { Button } from 'react-native-paper';
import { Picker } from '@react-native-picker/picker';
import UploadPhotoComp from './UploadPhotoComp';
import { CsrfTokenContext } from "./CsrfTokenContext";
import axios from "axios";

// Import the necessary dependencies from React Navigation
import { useNavigation } from '@react-navigation/native';

const rentOptions = [];
for (let i = 900; i <= 5000; i += 200) {
  rentOptions.push({ label: String(i), value: String(i) });
}

const roomsOptions = [];
for (let i = 1; i <= 6; i += 0.5) {
  roomsOptions.push({ label: String(i), value: String(i) });
}

const roommatesOptions = [];
for (let i = 1; i <= 4; i += 1) {
  roommatesOptions.push({ label: String(i), value: String(i) });
}

const toiletsOptions = [];
for (let i = 1; i <= 3; i += 1) {
  toiletsOptions.push({ label: String(i), value: String(i) });
}

const showersOptions = [];
for (let i = 1; i <= 3; i += 1) {
  showersOptions.push({ label: String(i), value: String(i) });
}


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


const SuccessProperty = ({ navigation, route }) => {
  // const navigation = useNavigation(); // Hook to access navigation object
  console.log("SuccessRoommate");
  console.log(route.params.username);
  const username = route.params.username;
  const csrfToken = useContext(CsrfTokenContext);
  const [country, setCountry] = useState('');
  const [city, setCity] = useState('');
  const [neighborhood, setNeighborhood] = useState('');
  const [floorNumber, setFloorNumber] = useState('');
  const [rent, setRent] = useState('');

  const [minRent, setMinRent] = useState('');
  const [maxRent, setMaxRent] = useState('');

  const [minRooms, setMinRooms] = useState('');
  const [maxRooms, setMaxRooms] = useState('');

  const [minRoommates, setMinRoommates] = useState('');
  const [maxRoommates, setMaxRoommates] = useState('');

  const [minToilets, setMinToilets] = useState('');
  const [maxToilets, setMaxToilets] = useState('');

  const [minShowers, setMinShowers] = useState('');
  const [maxShowers, setMaxShowers] = useState('');

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
  const [dealbreakerOptions, setDealbreakerOptions] = useState({
    renovated: false,
    shelter_inside: false,
    shelter_nearby: false,
    furnished: false,
    shared_living_room: false,
  });


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


  const dealbreakerOptionsList = [
    'Renovated property',
    'A Shelter inside',
    'A Shelter nearby',
    'Furnished property',
    'Shared living room',
  ];
  

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
    console.log('Floor Number:', floorNumber);
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

    navigation.navigate('IdealRoommate', {username: username}); // Navigate to the IdealRoommate screen
  };

  const handleNearbyOptionChange = (option) => {
    setNearbyOptions({ ...nearbyOptions, [option]: !nearbyOptions[option] });
  };

  const handleDealbreakerOptionChange = (option) => {
    setDealbreakerOptions({ ...dealbreakerOptions, [option]: !dealbreakerOptions[option] });
  };

  return (
    <KeyboardAvoidingView style={styles.container} behavior="padding">
      <ScrollView>
        <Text style={styles.title}>Enter your dream property details please</Text>

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
          <Text style={styles.label}>Floor Number:</Text>
            <TextInput
              value={floorNumber}
              onChangeText={setFloorNumber}
              style={styles.input}
            />
          </View>
        </View>



        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Rent range:</Text>
          <View style={styles.ageRangeContainer}>
            <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Min</Text>
              <View style={[styles.picker, minRent && styles.pickerSelected]}>
                <Picker selectedValue={minRent} onValueChange={setMinRent}>
                  {rentOptions.map((item, index) => (
                    <Picker.Item key={index} label={item.label} value={item.value} />
                  ))}
                </Picker>
              </View>
            </View>
            <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Max</Text>
              <View style={[styles.picker, maxRent && styles.pickerSelected]}>
                <Picker selectedValue={maxRent} onValueChange={setMaxRent}>
                  {rentOptions.map((item, index) => (
                    <Picker.Item key={index} label={item.label} value={item.value} />
                  ))}
                </Picker>
              </View>
            </View>
          </View>
        </View>

        

        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Number of rooms:</Text>
          <View style={styles.ageRangeContainer}>
            <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Min</Text>
              <View style={[styles.picker, minRooms && styles.pickerSelected]}>
                <Picker selectedValue={minRooms} onValueChange={setMinRooms}>
                  {roomsOptions.map((item, index) => (
                    <Picker.Item key={index} label={item.label} value={item.value} />
                  ))}
                </Picker>
              </View>
            </View>
            <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Max</Text>
              <View style={[styles.picker, maxRooms && styles.pickerSelected]}>
                <Picker selectedValue={maxRooms} onValueChange={setMaxRooms}>
                  {roomsOptions.map((item, index) => (
                    <Picker.Item key={index} label={item.label} value={item.value} />
                  ))}
                </Picker>
              </View>
            </View>
          </View>
        </View>


        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Number of roommates:</Text>
          <View style={styles.ageRangeContainer}>
            <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Min</Text>
              <View style={[styles.picker, minRoommates && styles.pickerSelected]}>
                <Picker selectedValue={minRoommates} onValueChange={setMinRoommates}>
                  {roommatesOptions.map((item, index) => (
                    <Picker.Item key={index} label={item.label} value={item.value} />
                  ))}
                </Picker>
              </View>
            </View>
            <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Max</Text>
              <View style={[styles.picker, maxRoommates && styles.pickerSelected]}>
                <Picker selectedValue={maxRoommates} onValueChange={setMaxRoommates}>
                  {roommatesOptions.map((item, index) => (
                    <Picker.Item key={index} label={item.label} value={item.value} />
                  ))}
                </Picker>
              </View>
            </View>
          </View>
        </View>

        <View style={styles.rowContainer}>
        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Number of toilets:</Text>
          <View style={styles.ageRangeContainer}>
            <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Min</Text>
              <View style={[styles.picker, minToilets && styles.pickerSelected]}>
                <Picker selectedValue={minToilets} onValueChange={setMinToilets}>
                  {toiletsOptions.map((item, index) => (
                    <Picker.Item key={index} label={item.label} value={item.value} />
                  ))}
                </Picker>
              </View>
            </View>
          </View>
        </View>


        <View style={styles.fieldContainer}>
          <Text style={styles.label}>Number of showers:</Text>
          <View style={styles.ageRangeContainer}>
            <View style={styles.pickerContainer}>
            <Text style={styles.pickerLabel}>Min</Text>
              <View style={[styles.picker, minShowers && styles.pickerSelected]}>
                <Picker selectedValue={minShowers} onValueChange={setMinShowers}>
                  {showersOptions.map((item, index) => (
                    <Picker.Item key={index} label={item.label} value={item.value} />
                  ))}
                </Picker>
              </View>
            </View>
          </View>
        </View>

        </View>

       
        <Text style={styles.nearbyOptionsLabel}>What is deal breaker for you?</Text>
        <View style={styles.nearbyOptionsContainer}>
          {dealbreakerOptionsList.map((option, index) => (
            <Text
              key={index}
              style={[styles.nearbyOption, nearbyOptions[option] && styles.nearbyOptionSelected]}
              onPress={() => handleNearbyOptionChange(option)}
            >
              {option}
            </Text>
          ))}
        </View>


        <Text style={styles.nearbyOptionsLabel}>What is critical to have near the property?</Text>
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
  pickerContainer: {
    flex: 1,
    marginRight: 8,
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
});

export default SuccessProperty;



// ##################################################################################################################
