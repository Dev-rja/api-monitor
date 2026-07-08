# API Reliability Monitor — SLA Report

> Last updated: **2026-07-08 00:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 79.94% | 2202.6 | 10206.7 | 1000ms | 267/1331 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 122.5 | 4595.4 | 1500ms | 4/1331 |
| ❌ | `nasa_apod` | 74.38% | 49.89% | 3354.5 | 11152.5 | 2000ms | 667/1331 |
| ❌ | `ipapi_check` | 76.41% | 99.92% | 154.9 | 4507.0 | 2500ms | 1/1331 |
| ❌ | `dog_ceo_random` | 94.74% | 96.84% | 530.3 | 10244.1 | 2500ms | 42/1331 |
| ⚠️ | `open_meteo_weather` | 98.57% | 96.92% | 733.2 | 14877.1 | 2000ms | 41/1331 |
| ⚠️ | `rest_countries` | 98.87% | 98.57% | 318.3 | 10221.5 | 2500ms | 19/1331 |
| ✅ | `useless_fact` | 99.62% | 99.7% | 632.9 | 10229.6 | 2500ms | 4/1331 |
| ✅ | `catfact_random` | 99.77% | 99.32% | 255.9 | 10080.2 | 3000ms | 9/1331 |
| ✅ | `coingecko_bitcoin` | 99.77% | 99.92% | 98.0 | 4328.4 | 1500ms | 1/1331 |
| ✅ | `agify_name` | 99.92% | 99.7% | 384.1 | 16112.2 | 2000ms | 4/1331 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 212.5 | 3882.8 | 2000ms | 2/1331 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4266.1 | 62.16% |
| `nasa_apod` | 09:00 | 4216.7 | 54.39% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 01:00 | 4125.5 | 58.97% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `nasa_apod` | 18:00 | 3843.5 | 54.29% |
| `nasa_apod` | 11:00 | 3669.9 | 54.17% |
| `nasa_apod` | 20:00 | 3574.9 | 50.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
