import React, { useState, useEffect } from 'react';
import { View, StyleSheet } from 'react-native';
import { TextInput, Button } from 'react-native-paper';
import { MaterialIcons } from '@expo/vector-icons';
import * as Font from 'expo-font';

const AdditionalInfoScreen = ({ navigation }) => {
  const [occupation, setOccupation] = useState(''); // 'Yes' or 'No'
  const [smoking, setSmoking] = useState(''); // 'Yes' or 'No'
  const [diet, setDiet] = useState(''); // 'Yes' or 'No'
  const [kosher, setKosher] = useState(''); // 'Yes' or 'No'
  const [single, setSingle] = useState(''); // 'Yes' or 'No'
  const [hospitality, setHospitality] = useState(''); // 'Yes' or 'No'
  const [sharingShopping, setSharingShopping] = useState(''); // 'Yes' or 'No'
  const [isFontLoaded, setIsFontLoaded] = useState(false);
  const [selection, setSelection] = useState('');


  useEffect(() => {
    const loadFonts = async () => {
      await Font.loadAsync({
        MaterialIcons: require('@expo/vector-icons/build/vendor/react-native-vector-icons/Fonts/MaterialIcons.ttf'),
      });
      setIsFontLoaded(true);
    };

    loadFonts();
  }, []);

  const handleSubmit = () => {
    // Perform logic with additional info
    console.log('Additional Info:', {
      occupation,
      smoking,
      diet,
      kosher,
      single,
      hospitality,
      sharingShopping,
    });
  
    // Navigate to the SelectionScreen and pass the selection
    navigation.navigate('Selection', { selection });
  };
  

  if (!isFontLoaded) {
    return null; // Render null or a loading indicator until the font is loaded
  }

  return (
    <View style={styles.container}>
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
          style={styles.input}
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
          style={styles.input}
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
          style={styles.input}
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
          style={styles.input}
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
          style={styles.input}
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
          style={styles.input}
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
          style={styles.input}
          editable={false}
        />
      </View>

      <Button mode="contained" onPress={handleSubmit} style={styles.button}>
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
  option: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  icon: {
    marginRight: 16,
  },
  input: {
    flex: 1,
  },
  button: {
    marginTop: 16,
  },
});

export default AdditionalInfoScreen;
