# API Reliability Monitor — SLA Report

> Last updated: **2026-05-04 06:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 58.44% | 4348.7 | 10206.7 | 1000ms | 261/628 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 122.8 | 4088.9 | 1500ms | 2/628 |
| ❌ | `nasa_apod` | 70.54% | 49.2% | 3559.0 | 10549.1 | 2000ms | 319/628 |
| ❌ | `ipapi_check` | 86.94% | 100.0% | 155.9 | 353.0 | 2500ms | 0/628 |
| ⚠️ | `rest_countries` | 98.57% | 98.25% | 342.7 | 10221.5 | 2500ms | 11/628 |
| ⚠️ | `open_meteo_weather` | 98.73% | 96.97% | 717.7 | 14877.1 | 2000ms | 19/628 |
| ⚠️ | `dog_ceo_random` | 99.52% | 93.31% | 709.8 | 10244.1 | 2500ms | 42/628 |
| ✅ | `catfact_random` | 99.52% | 99.36% | 254.9 | 10080.2 | 3000ms | 4/628 |
| ✅ | `coingecko_bitcoin` | 99.52% | 100.0% | 98.2 | 252.0 | 1500ms | 0/628 |
| ✅ | `useless_fact` | 99.68% | 99.36% | 589.6 | 10229.6 | 2500ms | 4/628 |
| ✅ | `agify_name` | 100.0% | 99.84% | 369.7 | 3237.1 | 2000ms | 1/628 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.68% | 236.9 | 3882.8 | 2000ms | 2/628 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 5605.3 | 54.55% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 12:00 | 5183.8 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `nasa_apod` | 17:00 | 4950.9 | 61.11% |
| `numbers_trivia` | 18:00 | 4840.2 | 46.43% |
| `numbers_trivia` | 10:00 | 4784.8 | 46.15% |
| `numbers_trivia` | 05:00 | 4708.1 | 45.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
