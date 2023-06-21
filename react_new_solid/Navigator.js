import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Roomit from './Roomit';
import Screen2 from './Screen2';
import Screen3 from './Screen3';
import SignIn from './SignIn';
import MainPage_ForARoomate from './MainPage_ForARoomate';
import ViewProfile from './ViewProfile';
import InboxPage from './InboxPage';
import SignUp1 from './SignUp1';
import SignUpScreen from './SignUpScreen';
import PersonalInfoScreen from './PersonalInfoScreen';
import AdditionalInfoScreen from './AdditionalInfoScreen';
import SuccessRoommate from './SuccessRoommate';
import SuccessProperty from './SuccessProperty';
import SelectionScreen from './SelectionScreen';
import UploadPhoto from './UploadPhoto';
import IdealRoommate from './IdealRoommate';
import RegistrationSuccess from './RegistrationSuccess';
import { useState, useEffect } from 'react';
import { CsrfTokenContext } from './CsrfTokenContext';
import axios from "axios"

const Stack = createStackNavigator();

const Navigator = () => {
  const [csrfToken, setCsrfToken] = useState();
  useEffect(() => {
    async function getCsrfToken() {
      const loginResponse = await axios.get('http://192.168.1.171:8000/user/get-csrf-token/');
      const csrfTokenHeader = loginResponse.headers['set-cookie']
        .find(cookie => cookie.startsWith('csrftoken'));
      if (csrfTokenHeader) {
        const csrfToken = csrfTokenHeader.split('=')[1].split(';')[0];
        setCsrfToken(csrfToken);
      }
    }
    getCsrfToken();
  }, []);

  return (
    <CsrfTokenContext.Provider value={csrfToken}>
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name="Roomit" component={Roomit} />
          <Stack.Screen name="Screen2" component={Screen2} />
          <Stack.Screen name="Screen3" component={Screen3} />
          <Stack.Screen name="SignIn" component={SignIn} />
          <Stack.Screen name="MainPage_ForARoomate" component={MainPage_ForARoomate} />
          <Stack.Screen name="ViewProfile" component={ViewProfile} />
          <Stack.Screen name="InboxPage" component={InboxPage} />
          <Stack.Screen name="SignUp1" component={SignUp1} />
          <Stack.Screen name="SignUpScreen" component={SignUpScreen} />
          <Stack.Screen name="PersonalInfo" component={PersonalInfoScreen} />
          <Stack.Screen name="AdditionalInfo" component={AdditionalInfoScreen} />
          <Stack.Screen name="SuccessProperty" component={SuccessProperty} />
          <Stack.Screen name="SuccessRoommate" component={SuccessRoommate} />
          <Stack.Screen name="Selection" component={SelectionScreen} />
          <Stack.Screen name="UploadPhoto" component={UploadPhoto} />
          <Stack.Screen name="IdealRoommate" component={IdealRoommate} />
          <Stack.Screen name="RegistrationSuccess" component={RegistrationSuccess} />
        </Stack.Navigator>
      </NavigationContainer>
    </CsrfTokenContext.Provider>
  );
};

export default Navigator;
