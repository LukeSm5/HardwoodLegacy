
import { View, Text, Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function LineupScreen() {
  const router = useRouter();
  return (
    <View>
      <Text>Lineup Screen</Text>
      <Button title="Back" onPress={() => router.back()}></Button>
    </View>
  );
}