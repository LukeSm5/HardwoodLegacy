import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack screenOptions={{ headerShown: false }}>
      <Stack.Screen name="(tabs)" />
      <Stack.Screen name="(tabs)/team/lineup" />
      <Stack.Screen name="(tabs)/team/injury" />
      <Stack.Screen name="(tabs)/team/playerDetail" />
      <Stack.Screen name="(tabs)/stats/teamStats" />
      <Stack.Screen name="(tabs)/stats/leaderboard" />
      <Stack.Screen name="(tabs)/stats/history" />
      <Stack.Screen name="(tabs)/stats/awards" />
    </Stack>
  );
}