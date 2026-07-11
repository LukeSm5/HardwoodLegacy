
import { View, Text, Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function LineupScreen() {
  const router = useRouter();
  /* TODO: Implement Lineup functionality
  1. Continue the roster from the roster screen, with number and name visible
  2. Implement a drag and drop functionality to move players into the starting lineup
  3. Add sliders to adjust the minutes played for each player in the lineup
  4. Create a button to automatically adjust the lineup based on player fatigue and injury status
*/
  return (
    <View>
      <Text>Lineup Screen</Text>
      <Button title="Back" onPress={() => router.back()}></Button>
    </View>
  );
}