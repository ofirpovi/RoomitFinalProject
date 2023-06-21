import React, { useEffect } from 'react';
import { FlatList, Image, StyleSheet, View, Text, TouchableOpacity } from 'react-native';
import axios from "axios";

const DATA = [
  {
    id: '1',
    image: require('./assets/Ido.jpg'),
    title: 'Ido Hersko',
    description: 'M.Sc. Student at Ben-Gurion University, 27 years old.',
  },
  {
    id: '2',
    image: require('./assets/Bar.jpg'),
    title: 'Bar Efrat',
    description: 'Industrial Engineer at Apple, 26 years old.',
  },
  {
    id: '3',
    image: require('./assets/Someone.jpg'),
    title: 'Sasha Levi',
    description: 'Laywer, 28 years old.',
  },
  // Add more images here...
];

const MyComponent = ({username}) => {
  // const dataFromServer = axios.post(server_url).then((result)=>{return result;})
  
  const renderItem = ({ item }) => {
    return (
        <View style={styles.item}>
          <Image
            source={item.image}
            style={styles.image}
          />
          <View style={styles.textContainer}>
            <Text style={styles.title}>{item.title}</Text>
            <Text style={styles.description}>{item.description}</Text>
          </View>
        </View>
      );
  };

  return (
    <View style={styles.container}>
      <FlatList
        data={DATA}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        horizontal={false}
      />
    </View>
  );
};

const MyScreen = ({ navigation, route }) => {
  // useEffect(async ()=>{
  //   await axios.get("http://192.168.1.171:8000/");
  // }, [])
  console.log("MainPage_ForARoommate");
  console.log(route.params.username);
  const username = route.params.username;
  const navigateToViewProfile = () => {
    navigation.navigate('ViewProfile', {username: username});
  };

  const navigateToAnotherScreen = () => {
    navigation.navigate('InboxPage', {username: username});
  };


  const server_url = `http://192.168.1.171:8000/requirementsR/${route.params.username}/`;

  return (
    <View style={styles.screen}>
      <View style={styles.bar}>
      <TouchableOpacity style={styles.button} onPress={navigateToAnotherScreen}>
          <Text style={styles.buttonText}>Inbox</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={navigateToViewProfile}>
          <Image source={require('./assets/yoav_square.jpg')} style={styles.profileIcon} />
        </TouchableOpacity>
      </View>
      <MyComponent username={route.params.username} />
    </View>
  );
};

const styles = StyleSheet.create({
  screen: {
    flex: 1,
  },
  bar: {
    height: 50,
    backgroundColor: 'pink',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 10,
  },
  profileIcon: {
    width: 40,
    height: 40,
    marginRight: 10,
    borderRadius: 100,
  },
  button: {
    backgroundColor: '#fff',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 10,
  },
  buttonText: {
    fontSize: 16,
  },
  container: {
    flex: 1,
  },
  item: {
    flex: 1,
    flexDirection: 'column',
    alignItems: 'center',
    marginVertical: 7,
  },
  image: {
    width: 420,
    height: 200,
    resizeMode: 'cover',
    borderRadius: 20,
  },
  textContainer: {
    flex: 1,
    marginVertical: 5,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  description: {
    fontSize: 13,
  },
});

export default MyScreen;
