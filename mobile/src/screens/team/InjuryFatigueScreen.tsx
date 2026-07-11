import { View, Text, Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function InjuryFatigueScreen() {
  const router = useRouter();
  /* TODO: Implement injury fatigue functionality
  1. Continue the roster from the roster screen, with number and name visible
  2. Add a fatigue status for each player, with a color-coded system (green, yellow, red)
  3. Add an injury status for each player, with a color-coded system (green, yellow, red)
  4. Add a pop-up for a player with red injury status, with a list of injuries and their severity
  5. Add a dropdown for each player to rest, practice, or play leading up to the next game
*/
  return (
    <View>
      <Text>Injury/Fatigue Screen</Text>      
      <Button title="Back" onPress={() => router.back()}></Button>
    </View>
  );
}