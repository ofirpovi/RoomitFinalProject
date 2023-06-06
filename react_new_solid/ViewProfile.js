import React from 'react';
import { FlatList, Image, StyleSheet, View, Text, TouchableOpacity } from 'react-native';
import { Icon } from 'react-native-elements';
import MaterialIcons from 'react-native-vector-icons/MaterialIcons';


const DATA = [
  {
    id: '1',
    image: require('./assets/yoav_rec.jpg'),
    title: 'Yoav Magrisso',
    description: 'Electro-Optical Engineer at Mobileye, 29 years old.',
  },
  // Add more images here...
];


const MyScreen = ({ navigation }) => {
    const navigateToAnotherScreen = () => {
      navigation.navigate('ViewProfile');
    };
  
    const renderItem = ({ item }) => {
        return (
            <View style={styles.container}>
                <View style={styles.item}>
                    <Image source={item.image} style={styles.image} />
                    <View style={styles.textContainer}>
                    <Text style={styles.title}>{item.title}</Text>
                    <Text style={styles.description}>{item.description}</Text>
                    <View style={styles.allIconsContainter}>
                    {/* <View style={styles.infoContainer}>
                        <Icon
                        name="phone"
                        type="font-awesome"
                        color="#517fa4"
                        size={20}
                        />
                        <Text style={styles.infoText}>+972 52-456-7891</Text>
                    </View>
                    <View style={styles.infoContainer}>
                        <MaterialIcons name="location-on" color="#517fa4" size={20} />
                        <Text style={styles.infoText}>123 Main St, Anytown USA</Text>
                    </View>
                    <View style={styles.infoContainer}>
                        <Icon
                        name="envelope"
                        type="font-awesome"
                        color="#517fa4"
                        size={20}
                        />
                        <Text style={styles.infoText}>yoav.magrisso@gmail.com</Text>
                    </View> */}
                    </View>
                    </View>
                </View>
            </View>
        );
      };
  
    return (
      <View style={styles.screen}>
        <FlatList
          data={DATA}
          renderItem={renderItem}
          keyExtractor={item => item.id}
          horizontal={false}
        />
      </View>
    );
  };


const styles = StyleSheet.create({
    screen: {
      flex: 1,
    },
    container: {
        flex: 1,
        textAlign: 'center',
        alignItems: 'center',
      },
    item: {
      flex: 1,
      flexDirection: 'column',
      alignItems: 'center',
      marginVertical: 7,
    },
    image: {
      width: 420,
      height: 280,
      resizeMode: 'cover',
      borderRadius: 20,
    },
    textContainer: {
      flex: 1,
      paddingTop: 20,
      width: '100%',
    },
    title: {
      fontSize: 25,
      fontWeight: 'bold',
      marginBottom: 5,
    },
    description: {
      fontSize: 14,
    },
    infoContainer: {
      flexDirection: 'row',
      alignItems: 'center',
      marginVertical: 20,
    },
    infoText: {
      fontSize: 16,
      marginLeft: 10,
      fontWeight: 'bold',
    },
    allIconsContainter: {
        marginLeft: 10,
        paddingTop: 40,
      },
  });

export default MyScreen;


// import React from 'react';
// import { View, Text, Image } from 'react-native';
// import Icon from 'react-native-vector-icons/FontAwesome';

// const MyScreen = () => {
//   return (
//     <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
//       <Image
//         source={require('./assets/yoav_rec.jpg')} // Replace with the actual image path
//         style={{ width: 200, height: 200 }}
//       />
//       <Text style={{ fontSize: 20, fontWeight: 'bold', marginTop: 10 }}>
//         Yoav Magrisso
//       </Text>
//       <Text style={{ fontSize: 16, marginTop: 5 }}>
//         Electro-Optical Engineer at Mobileye, 29 years old.
//       </Text>
//       <View style={{ flexDirection: 'row', marginTop: 20 }}>
//         <Icon
//           name="phone"
//           color="#000"
//           size={20}
//         />
//         <Text style={{ marginLeft: 10 }}>Phone Number: 123-456-7890</Text>
//       </View>
//       <View style={{ flexDirection: 'row', marginTop: 10 }}>
//         <Icon
//           name="envelope"
//           color="#000"
//           size={20}
//         />
//         <Text style={{ marginLeft: 10 }}>Email: yoav.magrisso@example.com</Text>
//       </View>
//     </View>
//   );
// };

// export default MyScreen;
