import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="stats" options={{ title: 'Stats', headerShown: false }} />
      <Tabs.Screen name="schedule" options={{ title: 'Schedule', headerShown: false }} />
      <Tabs.Screen name="dashboard" options={{ title: 'Dashboard', headerShown: false }} />
      <Tabs.Screen name="team" options={{ title: 'Team', headerShown: false }} />
      <Tabs.Screen name="recruiting" options={{ title: 'Recruiting', headerShown: false }} />
    </Tabs>
  );
}