import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack screenOptions={{ headerShown: false }}>
      <Stack.Screen name="(tabs)" />
      <Stack.Screen name="(tabs)/team/lineup" />
      <Stack.Screen name="(tabs)/team/injury" />
      <Stack.Screen name="(tabs)/team/playerDetail" />
    </Stack>
  );
}