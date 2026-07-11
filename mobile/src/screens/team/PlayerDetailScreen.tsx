import { View, Text, Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function PlayerDetailScreen() {
  const router = useRouter();
  /* TODO: Implement player detail functionality
    1. When the player is selected from the roster screen, the player detail screen should appear
    2. Top
      a. Player name
      b. Player Number
      c. Player Position
      d. Player Year of School
      e. Player Hometown
      f. Player Age
    3. Middle
        a. Player Injury/Fatigue Status
        b. Player Height
        c. Player Weight
        d. Player Stats
        e. Player History
    4. Bottom
        a. Player Awards
        b. Player Scholarship Status
*/
  return (
    <View>
      <Text>Player Detail Screen</Text>
      <Button title="Back" onPress={() => router.back()}></Button>
    </View>
  );
}