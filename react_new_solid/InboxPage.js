import React, { useState, useEffect } from 'react';
import { View, Text, Image, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
// import FaceDetector from '@react-native-community/face-detector';

const InboxPage = ({ navigation, route }) => {
  const username = route.params.username;
  // const navigateToAnotherScreen = () => {
  //   navigation.navigate('MainPage_for', {username: username});
  // };
  const inboxItems = [
    { id: '1', name: 'John Doe', message: 'Hello, how are you?', avatar: require('./assets/Ido.jpg') },
    { id: '2', name: 'Jane Smith', message: 'Can you meet me at 5pm today?', avatar: require('./assets/Bar.jpg') },
    { id: '3', name: 'Bob Johnson', message: 'Don\'t forget to submit the report by tomorrow', avatar: require('./assets/Someone.jpg') },
    // Add more inbox items here...
  ];

  const [avatarDimensions, setAvatarDimensions] = useState(null);

  const renderInboxItem = ({ item }) => {
    const avatarStyle = {
      width: avatarDimensions?.width ?? 40,
      height: avatarDimensions?.height ?? 40,
      borderRadius: avatarDimensions?.width ? avatarDimensions.width / 2 : 20,
      backgroundColor: 'gray',
      overflow: 'hidden',
    };

    return (
      <TouchableOpacity style={styles.inboxItem}>
        <View style={styles.avatarContainer}>
          <Image
            source={item.avatar}
            style={avatarStyle}
            onLayout={({ nativeEvent }) => {
              setAvatarDimensions(nativeEvent.layout);
            }}
          />
        </View>
        <View style={styles.inboxItemContent}>
          <Text style={styles.inboxItemTitle}>{item.name}</Text>
          <Text numberOfLines={1} style={styles.inboxItemMessage}>{item.message}</Text>
        </View>
      </TouchableOpacity>
    );
  };

  const handleFacesDetected = ({ faces }) => {
    if (faces.length > 0 && avatarDimensions) {
      const { x, y, width, height } = faces[0].bounds;
      const scaleFactor = avatarDimensions.width / width;
      const left = x * scaleFactor;
      const top = y * scaleFactor;
      const avatarContainerStyle = {
        position: 'absolute',
        left: avatarDimensions.width / 2 - left - avatarDimensions.width / 2,
        top: avatarDimensions.height / 2 - top - avatarDimensions.height / 2,
      };
      return (
        <View style={[styles.avatarContainer, avatarContainerStyle]}>
          <Image source={inboxItems[0].avatar} style={[styles.avatar, avatarDimensions]} />
        </View>
      );
    } else {
      return null;
    }
  };

  return (
    <View style={styles.container}>
      <FlatList
        data={inboxItems}
        renderItem={renderInboxItem}
        keyExtractor={item => item.id}
        contentContainerStyle={styles.inboxList}
      />
      {/* <FaceDetector
        style={styles.faceDetector}
        onFacesDetected={handleFacesDetected}
        mode={FaceDetector.Constants.Mode.accurate}
        minDetectionInterval={1000}
        trackingEnabled={true}
      /> */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 50,
  },
  inboxList: {
    padding: 10,
  },
  inboxItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#f5f5f5',
    borderRadius: 10,
    padding: 10,
    marginVertical: 5,
  },
  avatarContainer: {
    marginRight: 10,
  },
  avatar: {
    width: 40,
    height: 40,
    borderRadius: 20,
  },
  inboxItemContent: {
    flex: 1,
  },
  inboxItemTitle: {
    fontWeight: 'bold',
    fontSize: 16,
    marginBottom: 5,
  },
  inboxItemMessage: {
    fontSize: 14,
  },
  faceContainer: {
    width: 40,
    height: 40,
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
    overflow: 'hidden',
    backgroundColor: 'lightgray',
    marginRight: 10,
  },
  face: {
    width: 36,
    height: 36,
    borderRadius: 18,
  },
});



export default InboxPage;