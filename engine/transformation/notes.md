# Transformations
- Scaling
- Translating
- Rotating

Will be done via matrix multiplication

### Scale
(x, y, z) -> (ax, by, cz)

##### Scale Matrix
| a | 0 | 0 | 0 |
| 0 | b | 0 | 0 |
| 0 | 0 | c | 0 |
| 0 | 0 | 0 | d |

### Translate
(x, y, z) -> (x + a, y + b, c + z)

##### Translation Matrix
| 1 | 0 | 0 | a |
| 0 | 1 | 0 | b |
| 0 | 0 | 1 | c |
| 0 | 0 | 0 | 1 |

### Rotate
(x, y, z) -> (x cos(theta) - y sin(theta), y cos(theta) + x sin(theta), z)

##### Rotation Matrix About Z-Axis
| cos(theta) | -sin(theta) | 0 | 0 |
| sin(theta) | cos(theta) | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 | 

##### Rotation Matrix About X-Axis
| 1 | 0 | 0 | 0 |
| 0 | cos(theta) | -sin(theta) | 0 |
| 0 | sin(theta) | cos(theta) | 0 |
| 0 | 0 | 0 | 1 |

##### Rotation Matrix About Y-Axis
| cos(theta) | 0 | sin(theta) | 0 |
| 0 | 1 | 0 | 0 |
| -sin(theta) | 0 | cos(theta) | 0 |
| 0 | 0 | 0 | 1 |


