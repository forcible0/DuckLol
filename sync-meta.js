/**
 * DuckLoL Meta Sync & Database Generator
 * Updates champion builds, runes, items, spells, skill orders, win rates, and matchups.
 */

const { execSync } = require('child_process');

console.log('🔄 Syncing DuckLoL metadata with Patch 16.16.1...');

try {
  execSync('python3 sync_meta.py', { stdio: 'inherit' });
  console.log('✨ Meta sync completed successfully! data.json is up-to-date.');
} catch (err) {
  console.error('❌ Error during meta sync:', err.message);
}
