const { contextBridge } = require('electron');

// Güvenli API expose et (şu anlık boş, ileride eklenebilir)
contextBridge.exposeInMainWorld('electronAPI', {
  platform: process.platform
});
