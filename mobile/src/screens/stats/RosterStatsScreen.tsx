import { View, Text, Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function RosterStatsScreen() {
  const router = useRouter();
  return (
    <View>
      <Text>Roster Stats Screen</Text>
      <Button title="Team Stats" onPress={() => router.push('/stats/teamStats')}></Button>
      <Button title="Leaderboard" onPress={() => router.push('/stats/leaderboard')}></Button>
      <Button title="History" onPress={() => router.push('/stats/history')}></Button>
      <Button title="Awards" onPress={() => router.push('/stats/awards')}></Button>
    </View>
  );
}