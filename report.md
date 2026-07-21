# API Reliability Monitor — SLA Report

> Last updated: **2026-07-21 01:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.36% | 1964.6 | 10206.7 | 1000ms | 268/1519 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 122.8 | 4595.4 | 1500ms | 4/1519 |
| ❌ | `ipapi_check` | 72.22% | 99.93% | 152.4 | 4507.0 | 2500ms | 1/1519 |
| ❌ | `nasa_apod` | 76.7% | 52.73% | 3115.5 | 11152.5 | 2000ms | 718/1519 |
| ⚠️ | `dog_ceo_random` | 95.06% | 96.25% | 563.5 | 10244.1 | 2500ms | 57/1519 |
| ⚠️ | `open_meteo_weather` | 98.75% | 97.3% | 712.9 | 14877.1 | 2000ms | 41/1519 |
| ✅ | `rest_countries` | 99.01% | 98.68% | 304.6 | 10221.5 | 2500ms | 20/1519 |
| ✅ | `useless_fact` | 99.67% | 99.74% | 635.7 | 10229.6 | 2500ms | 4/1519 |
| ✅ | `catfact_random` | 99.8% | 99.41% | 255.7 | 10080.2 | 3000ms | 9/1519 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 97.0 | 4328.4 | 1500ms | 1/1519 |
| ✅ | `agify_name` | 99.93% | 99.74% | 385.0 | 16112.2 | 2000ms | 4/1519 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 204.6 | 3882.8 | 2000ms | 2/1519 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4339.2 | 75.0% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 3891.8 | 50.79% |
| `nasa_apod` | 17:00 | 3842.7 | 52.56% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 11:00 | 3496.8 | 51.19% |
| `nasa_apod` | 01:00 | 3487.7 | 50.0% |
| `nasa_apod` | 12:00 | 3477.2 | 53.03% |
| `nasa_apod` | 18:00 | 3369.2 | 47.56% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
