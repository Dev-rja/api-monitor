# API Reliability Monitor — SLA Report

> Last updated: **2026-07-08 09:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.99% | 2198.1 | 10206.7 | 1000ms | 267/1334 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 122.5 | 4595.4 | 1500ms | 4/1334 |
| ❌ | `nasa_apod` | 74.44% | 49.93% | 3349.7 | 11152.5 | 2000ms | 668/1334 |
| ❌ | `ipapi_check` | 76.31% | 99.93% | 154.9 | 4507.0 | 2500ms | 1/1334 |
| ❌ | `dog_ceo_random` | 94.75% | 96.85% | 529.7 | 10244.1 | 2500ms | 42/1334 |
| ⚠️ | `open_meteo_weather` | 98.58% | 96.93% | 733.0 | 14877.1 | 2000ms | 41/1334 |
| ⚠️ | `rest_countries` | 98.88% | 98.58% | 318.1 | 10221.5 | 2500ms | 19/1334 |
| ✅ | `useless_fact` | 99.63% | 99.7% | 633.0 | 10229.6 | 2500ms | 4/1334 |
| ✅ | `catfact_random` | 99.78% | 99.33% | 255.8 | 10080.2 | 3000ms | 9/1334 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 98.0 | 4328.4 | 1500ms | 1/1334 |
| ✅ | `agify_name` | 99.93% | 99.7% | 384.0 | 16112.2 | 2000ms | 4/1334 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 212.4 | 3882.8 | 2000ms | 2/1334 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4792.7 | 80.95% |
| `nasa_apod` | 05:00 | 4266.1 | 62.16% |
| `nasa_apod` | 09:00 | 4153.2 | 53.45% |
| `nasa_apod` | 01:00 | 4125.5 | 58.97% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `numbers_trivia` | 03:00 | 4003.6 | 38.1% |
| `nasa_apod` | 18:00 | 3843.5 | 54.29% |
| `nasa_apod` | 11:00 | 3669.9 | 54.17% |
| `nasa_apod` | 20:00 | 3574.9 | 50.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
