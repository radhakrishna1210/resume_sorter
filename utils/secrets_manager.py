import streamlit as st
from pathlib import Path
import os

class SecretsManager:
    
    def __init__(self):
        self.sections = {}
        self.load_secrets()
    
    def load_secrets(self):
        try:
            # First, check environment variables (for Render/other hosting platforms)
            api_key_from_env = os.getenv('GEMINI_API_KEY')
            
            if api_key_from_env:
                # Use environment variable if available
                self.sections['gemini'] = {'api_key': api_key_from_env}
                return
            
            # Then check Streamlit secrets (for Streamlit Cloud)
            if hasattr(st, 'secrets'):
                if 'gemini' in st.secrets:
                    self.sections['gemini'] = st.secrets['gemini']
                    return
            else:
                self._ensure_local_secrets_file()
                
                try:
                    if 'gemini' in st.secrets:
                        self.sections['gemini'] = st.secrets['gemini']
                        return
                except (KeyError, AttributeError):
                    pass
            
            # If no secrets found, warn user
            st.warning("Gemini API credentials not found in secrets or environment variables.")
            self.sections = {}
        except Exception as e:
            st.error(f"Error loading secrets: {e}")
            self.sections = {}
    
    def get_secret(self, key, default=None, section='gemini'):
        # Check environment variable first (for Render)
        if key == 'api_key' and section == 'gemini':
            env_key = os.getenv('GEMINI_API_KEY')
            if env_key:
                return env_key
                
        if section in self.sections:
            return self.sections[section].get(key, default)
        return default
    
    def has_secrets(self, section='gemini'):
        # Check environment variable first
        if os.getenv('GEMINI_API_KEY'):
            return True
            
        required_keys = ['api_key']
        section_data = self.sections.get(section, {})
        
        return all(key in section_data 
                  and section_data[key] 
                  and section_data[key] != "your_gemini_api_key_here" 
                  for key in required_keys)
    
    def has_secret(self, key, section='gemini'):
        # Check environment variable first
        if key == 'api_key' and section == 'gemini':
            if os.getenv('GEMINI_API_KEY'):
                return True
                
        if section in self.sections:
            return (key in self.sections[section] 
                   and self.sections[section][key] 
                   and self.sections[section][key] != "your_gemini_api_key_here")
        return False
    
    def _ensure_local_secrets_file(self):
        secrets_dir = Path('.streamlit')
        secrets_file = secrets_dir / 'secrets.toml'
        
        if not secrets_file.exists():
            secrets_dir.mkdir(exist_ok=True)
            
            with open(secrets_file, 'w') as f:
                f.write("""
# Google Gemini API credentials
[gemini]
api_key = "your_gemini_api_key_here"
                """)
            
            st.warning("""
            A template secrets.toml file has been created in the .streamlit directory.
            Please edit this file to add your Gemini API key.
            """)