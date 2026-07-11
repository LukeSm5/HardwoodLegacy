import { View, Text, Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function RosterScreen() {
  const router = useRouter();
  return (
    <View>
      <Text>Roster Screen</Text>
      <Button title="Lineup" onPress={() => router.push('/team/lineup')}></Button>
      <Button title="Injury" onPress={() => router.push('/team/injury')}></Button>
      <Button title="Player Detail" onPress={() => router.push('/team/playerDetail')}></Button>
    </View>
  );
}