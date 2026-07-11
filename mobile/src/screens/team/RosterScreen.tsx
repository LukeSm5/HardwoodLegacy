import { View, Text, Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function RosterScreen() {
  const router = useRouter();
/* TODO: Implement roster functionality
  1. Create a list of players with names, numbers, positions, year of school, and height
  2. Add a button to view the lineup of the team
  3. Add a button to view the injury/fatigue status of the team
  4. Add a button to view the details of a specific player
    a. Includes stats, hometown, age, height, weight, awards, history, and other relevant information
    b. Add a button to offer a scholarship to a player
    c. Add a button to rescind a scholarship offer
    d. Add a button to release a player from the team
        i. Provide reason for release (e.g., injury, performance, disciplinary action)
  5. Sort by position, year of school, or height
*/
  return (
    <View>
      <Text>Roster Screen</Text>
      <Button title="Lineup" onPress={() => router.push('/team/lineup')}></Button>
      <Button title="Injury" onPress={() => router.push('/team/injury')}></Button>
      <Button title="Player Detail" onPress={() => router.push('/team/playerDetail')}></Button>
    </View>
  );
}