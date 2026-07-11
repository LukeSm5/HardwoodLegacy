import { View, Text, Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function InjuryFatigueScreen() {
  const router = useRouter();
  return (
    <View>
      <Text>Injury/Fatigue Screen</Text>      
      <Button title="Back" onPress={() => router.back()}></Button>
    </View>
  );
}