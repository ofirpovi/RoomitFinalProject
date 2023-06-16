import { AppLoading } from 'expo';
import React, { useState, useEffect } from 'react';
import Navigator from './Navigator';
import * as Font from 'expo-font';

const App = () => {
  const [fontLoaded, setFontLoaded] = useState(false);
  const [csrfToken, setCsrfToken] = useState();

  useEffect(() => {
    async function loadFonts() {
      await Font.loadAsync({
        'Courgette-Regular': require('./assets/fonts/Courgette-Regular.ttf'),
      });
      setFontLoaded(true);
    }
    loadFonts();
  }, []);

  if (!fontLoaded) {
    return null; // Return null while the font is loading
  }

  return (
      <Navigator />
  )
};

export default App;
