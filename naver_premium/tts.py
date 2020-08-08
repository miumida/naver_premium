import asyncio
import logging

import aiohttp
import async_timeout
import voluptuous as vol

from homeassistant.components.tts import CONF_LANG, PLATFORM_SCHEMA, Provider
from homeassistant.const import CONF_API_KEY, HTTP_OK
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

NAVER_PREMIUM_URL = "https://naveropenapi.apigw.ntruss.com/voice-premium/v1/tts"
CONF_VOICE = "voice"
DEFAULT_VOICE = "nara"
SUPPORT_VOICES = [
    "nara",
]

CONF_CLIENT_ID = "client_id"
CONF_CLIENT_SECRET = "client_secret"

CONF_SPEED = "speed"
DEFAULT_SPEED = 0
MIN_SPEED = -5
MAX_SPEED = 5
SPEED_SCHEMA = vol.All(vol.Coerce(int), vol.Clamp(min=MIN_SPEED, max=MAX_SPEED))

CONF_PITCH = "pitch"
DEFAULT_PITCH = 0
MIN_PITCH = -5
MAX_PITCH = 5
PITCH_SCHEMA = vol.All(vol.Coerce(int), vol.Clamp(min=MIN_PITCH, max=MAX_PITCH))

CONF_EMOTION = "emotion"
DEFAULT_EMOTION = 0
MIN_EMOTION = 0
MAX_EMOTION = 2
EMOTION_SCHEMA = vol.All(vol.Coerce(int), vol.Clamp(min=MIN_EMOTION, max=MAX_EMOTION))

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_CLIENT_ID): cv.string,
        vol.Required(CONF_CLIENT_SECRET): cv.string,
        vol.Optional(CONF_VOICE, default=DEFAULT_VOICE): vol.In(SUPPORT_VOICES),
        vol.Optional(CONF_SPEED, default=DEFAULT_SPEED): SPEED_SCHEMA,
        vol.Optional(CONF_PITCH, default=DEFAULT_PITCH): PITCH_SCHEMA,
        vol.Optional(CONF_EMOTION, default=DEFAULT_EMOTION): EMOTION_SCHEMA,
    }
)

def get_engine(hass, config, discovery_info=None):
    """Set up naver_tts_premium speech component."""
    return Naver_Premium(hass, config)

class Naver_Premium(Provider):
    """The Naver_TTS_Premium speech API provider."""

    def __init__(self, hass, config):
        """Init Naver_Premium TTS service."""
        self.hass = hass
        self.client_id = config.get(CONF_CLIENT_ID)
        self.client_secret = config.get(CONF_CLIENT_SECRET)
        self.voice = config.get(CONF_VOICE)
        self.speed = config.get(CONF_SPEED)
        self.pitch = config.get(CONF_PITCH)
        self.emotion = config.get(CONF_EMOTION)
        self.name = "Naver_TTS_Premium"
        self.headers = {
            "X-NCP-APIGW-API-KEY-ID": self.client_id,
            "X-NCP-APIGW-API-KEY" : self.client_secret,
        }

    @property
    def default_language(self):
        """Return the default language."""
        return "ko"

    @property
    def supported_languages(self):
        """Return list of supported languages."""
        return ["ko",]

    async def async_get_tts_audio(self, message, language, options=None):
        """Load TTS from naver_tts_premium."""
        websession = async_get_clientsession(self.hass)
        options = options or {}

        try:
            with async_timeout.timeout(10):
                data = {
                    "speaker" : options.get(CONF_VOICE, self.voice),
                    "volume" : 0,
                    "speed" : self.speed,
                    "pitch" : self.pitch,
                    "emotion" : options.get(CONF_EMOTION, self.emotion),
                    "format" : "mp3",
                    "text" : message,
                }

                request = await websession.post(NAVER_PREMIUM_URL, data=data, headers=self.headers)

                if request.status != HTTP_OK:
                    _LOGGER.error(
                        "Error %d on load URL %s", request.status, request.url
                    )
                    return (None, None)
                data = await request.read()
        
        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Timeout for Naver_tts_Premium speech API")
            return (None, None)

        return ("mp3", data)