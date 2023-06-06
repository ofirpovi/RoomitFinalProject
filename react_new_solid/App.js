// import React from 'react';
// import {View, Text, Image, ScrollView, TextInput} from 'react-native';

// const App = () => {
//   return (
//     <ScrollView>
//       <Text>Some text :)))))))))</Text>
//       <View>
//         <Text>Some more text</Text>
//         <Image
//           source={{
//             uri: 'https://reactnative.dev/docs/assets/p_cat2.png',
//           }}
//           style={{width: 200, height: 200}}
//         />
//       </View>
//       <TextInput
//         style={{
//           height: 40,
//           borderColor: 'gray',
//           borderWidth: 1,
//         }}
//         defaultValue="You can type in me"
//       />
//     </ScrollView>
//   );
// };

// export default App;


// // import { StatusBar } from 'expo-status-bar';
// // import { StyleSheet, Text, View } from 'react-native';

// // export default function App() {
// //   return (
// //     <View style={styles.container}>
// //       <Text>Hello world!</Text>
// //       <StatusBar style="auto" />
// //     </View>
// //   );
// // }

// // const styles = StyleSheet.create({
// //   container: {
// //     flex: 1,
// //     backgroundColor: '#fff',
// //     alignItems: 'center',
// //     justifyContent: 'center',
// //   },
// // });


// import React from 'react';
// import Navigator from './Navigator';
// import * as Font from 'expo-font';


// const App = () => {
//   return <Navigator />;
// };

// // Define a mapping of font names to their corresponding font files
// const customFonts = {
//   'Courgette-Regular': require('./assets/fonts/Courgette-Regular.ttf'),
// };

// // Load the custom fonts using Font.loadAsync
// async function loadFonts() {
//   await Font.loadAsync(customFonts);
// }

// // Call the loadFonts function when your app starts
// loadFonts();

// export default App;

import { AppLoading } from 'expo';
import React, { useState, useEffect } from 'react';
import Navigator from './Navigator';
import * as Font from 'expo-font';

const App = () => {
  const [fontLoaded, setFontLoaded] = useState(false);

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

  return <Navigator />;
};

export default App;
