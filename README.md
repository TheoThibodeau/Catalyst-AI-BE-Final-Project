# Catalyst BE ReadME 


https://catalyst-x226.onrender.com


**Token Authentication System**
* Djoser
* Docs: https://djoser.readthedocs.io/en/latest/introduction.html
  
**Deployment**
* Render
* Database: Postgresql@14
* Docs: https://render.com/docs/deploy-django
</br>
</br>


**CREATE USER**
> https://catalyst-x226.onrender.com/auth/users/

*request*
```json
POST  auth/users/
```
```json
    {
    "username": "superuser",
    "password": "somepassword"
    }
```

*response*
```json
HTTP_201_created
```
```json
    {
    "username": "superuser",
    "password": "somepassword",
    // "id": 1
    }
```
</br>
</br>

**LOGIN**
> https://catalyst-x226.onrender.com/auth/token/login/

*request*
```json
token create
```
```json
POST auth/token/login/
```
```json
    {
    "username": "superuser",
    "password": "somepassword"
    }
```

*response*
```json
HTTP_200_OK
```
```json
    {
    "auth_token": "somereallylonglistofnumbersandletters"
    }
```
</br>
</br>


**LOGOUT**
> https://catalyst-x226.onrender.com/auth/token/logout/

*request*
```json
token destroy
```
```json
POST auth/token/logout/
```

*response*
```json
HTTP_204_NO_CONTENT
```

</br>
</br>

**PROFILE**
> https://catalyst-x226.onrender.com/api/profile/username/

*request*
```json
GET api/profile/<username>/
```

*response*
```json
    {
    "username": "superuser",
    }
```
*request*
```json
PATCH  api/profile/<username>/
```

*response*
```json
    {
    "username": "superuser"
    },
```

*request*
```json
DELETE  api/profile/<username>/
```

*response*
```json
HTTP_204_NO_CONTENT
```

</br>
</br>

**WRITE PROMPT GENERATE**
> https://catalyst-x226.onrender.com/api/write/generate/

*request*
```json
POST api/write/generate/
```
```json
    {
    "style": "poem",   
	"theme": "emotion",
	"category": "relationships and love",
	"sentiment": "harmony",
	"emotion": "joy",
	"prompt_length": "prompt", 
        "temperature": 1,
	"user": 1
    }
```
</br>
</br>

**WRITE PROMPT GENERATE**
> https://catalyst-x226.onrender.com/api/response/write/id
```json
Output from openai api
```

```json
GET api/response/write/<id>
```
*response*
```json
    {
	"id": 45,
	"theme": "exploration",
	"category": "advocacy",
	"sentiment": "resilience",
	"emotion": "grief",
	"prompt_length": "prompt", 
        "temperature": 1,
	"output": "Uncharted horizons etch the undeniable path of your journey, as you champion for voices and navigate turmoil of crossed skies; poetry unfolds within your steadfast pilgrimage of sorrow and renewal.",
	"user": 1
    }
```
</br>
</br>

**GET ALL WRITE PROMPTS**
```json
GET api/write/prompts
```

**VISUAL ART PROMPT GENERATE**
> https://catalyst-x226.onrender.com/api/visual_art/generate/
```json
POST api/visual_art/generate/
```
```json
    {
	"medium": "painting",
	"theme": "texture",
	"sentiment": "renewal",
	"emotion": "joy",
	"temperature": 1.0,
        "prompt_length": "prompt", 
	"user": 1, 
	"output": ""
    }
```

**VISUAL ART PROMPT GET**
> https://catalyst-x226.onrender.com/api/response/visual_art/id
```json
Output from openai api
```

```json
GET api/response/visual_art/id
```
```json
    {
	"id": 25,
	"medium": "painting",
	"theme": "texture",
	"sentiment": "renewal",
	"emotion": "joy",
	"temperature": 1,
        "prompt_length": "prompt", 
	"output": "Create a vibrant masterpiece capturing the essence of transformation and delight, where layered brushstrokes evoke both tactile and emotional sensations.",
	"user": 1
    }
```
</br>
</br>

**GET ALL VISUAL ART PROMPTS**
```json
GET api/visual_art/prompts
```

**MOVEMENT PROMPT GENERATE**
> https://catalyst-x226.onrender.com/api/movement/generate/

```json
POST api/movement/generate/
```
```json
    {
	"theme": "spatial awareness",
	"somatic": "breath and movement",
	"sentiment": "harmony",
	"emotion": "joy",
	"temperature": 1,
        "prompt_length": "prompt", 
	"user": 1
    }
```
**MOVEMENT PROMPT GET**
> https://catalyst-x226.onrender.com/api/response/movement/id
```json
Output from openai api
```
```json
GET api/response/movement/id
```
```json
    {
	"id": 5,
	"theme": "spatial awareness",
	"somatic": "breath and movement",
	"sentiment": "harmony",
	"emotion": "joy",
	"temperature": 1,
        "prompt_length": "prompt", 
	"output": "Explore the depths of emotion, capturing the essence of longing and vulnerability, through fluid movements that merge strength and delicacy in a captivating dance.",
	"user": 1
    }
```
</br>
</br>

**GET ALL MOVEMENT PROMPTS**
```json
GET api/movement/prompts/
```

**MUSIC PROMPT GENERATE**
> https://catalyst-x226.onrender.com/api/music/generate/
```json
POST api/music/generate/
```
```json
    {
	"exploration": "musical time travel",
	"concept": "tempo",
	"element": "fire",
	"emotion": "joy",
	"temperature": 1,
        "prompt_length": "prompt", 
	"output": "",
	"user": 1
    }
```

**MUSIC PROMPT GET**
> https://catalyst-x226.onrender.com/api/response/music/id
```json
Output from openai api
```
```json
GET api/response/music/id
```
```json
    {
	"id": 2,
	"exploration": "musical time travel",
	"concept": "tempo",
	"element": "fire",
	"emotion": "joy",
	"temperature": 1,
        "prompt_length": "prompt",
	"output": "Journey through melodic epochs fuelled by celebratory rhythms, kindling a passionate storm. Create harmonies that transport listeners through a timeless musical dimension.",
	"user": 1
    }
```
</br>
</br>

**GET ALL MUSIC PROMPTS**
```json
GET api/music/prompts/
```

**USER PROMPT ARCHIVE LIST**
> https://catalyst-x226.onrender.com/api/prompt/archive/
```json
GET api/prompt/archive/
```

```json
[
    {
    "username": "superuser",
    }
    "music": [
        {
        "id": 2,
        "exploration": "musical time travel",
        "concept": "tempo",
        "element": "fire",
        "emotion": "joy",
	"temperature": 1,
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "Journey through melodic epochs fuelled by celebratory rhythms, kindling a passionate storm. Create harmonies that transport listeners through a timeless musical dimension.",
        "user": 1
	},
    ],
    "visual_arts": [
	{
	"id": 25,
	"medium": "painting",
	"theme": "texture",
	"sentiment": "renewal",
	"emotion": "joy",
	"temperature": 1.,
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "Create a vibrant masterpiece capturing the essence of transformation and delight, where layered brushstrokes evoke both tactile and emotional sensations.",
	"user": 1
	},
    ],
    "movements": [
	{
	"id": 5,
	"theme": "spatial awareness",
	"somatic": "breath and movement",
	"sentiment": "harmony",
	"emotion": "joy",
	"temperature": 1,
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "Create a dynamic dance piece that explores the seamless interplay of bodies in space, flowing breath, and expressive movements, evoking a sense of pure and radiant bliss.",
	"user": 1
        },	
    ],
    "writes": [
	{
        "id": 66,
        "style": "word play",
        "theme": "emotion",
        "category": "relationships and love",
        "sentiment": "renewal",
        "emotion": "joy",
        "temperature": 1,
        "prompt_length": "one word",
        "input_length": "Let the prompt be only 1 word",
        "output": "Spark",
        "user": 1
        },
    ]
]
```

**CREATE NOTE**
```json
POST api/note/create/
```

**RETRIEVE NOTE**
```json
GET api/note/id
```


**WELCOME PROMPT GENERATE**
```json
POST api/welcome/generate/
```

**RETRIEVE WELCOME PROMPT**
```json
GET api/welcome/id
```
