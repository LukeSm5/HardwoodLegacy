import { View, Text, Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function PlayerDetailScreen() {
  const router = useRouter();
  return (
    <View>
      <Text>Player Detail Screen</Text>
      <Button title="Back" onPress={() => router.back()}></Button>
    </View>
  );
}