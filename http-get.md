
## Server: Response
`script.py`
```python
```
```bash
$ uvicorn script:app --reload
```

## Client: Request

```kts
USE {
    repositories {
        mavenCentral()
    }
    dependencies {
        implementation("com.squareup.retrofit2:retrofit:2.9.0")
        implementation("com.squareup.retrofit2:converter-gson:2.9.0")
        implementation("com.squareup.retrofit2:converter-scalars:2.9.0")
        implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
    }
}
```
```kts
```
