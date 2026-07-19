# API Reliability Monitor — SLA Report

> Last updated: **2026-07-19 14:12 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.16% | 1984.5 | 10206.7 | 1000ms | 267/1497 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.7 | 4595.4 | 1500ms | 4/1497 |
| ❌ | `ipapi_check` | 72.75% | 99.93% | 152.6 | 4507.0 | 2500ms | 1/1497 |
| ❌ | `nasa_apod` | 76.35% | 52.17% | 3151.3 | 11152.5 | 2000ms | 716/1497 |
| ⚠️ | `dog_ceo_random` | 95.06% | 96.26% | 561.2 | 10244.1 | 2500ms | 56/1497 |
| ⚠️ | `open_meteo_weather` | 98.73% | 97.26% | 714.6 | 14877.1 | 2000ms | 41/1497 |
| ✅ | `rest_countries` | 99.0% | 98.73% | 303.7 | 10221.5 | 2500ms | 19/1497 |
| ✅ | `useless_fact` | 99.67% | 99.73% | 635.7 | 10229.6 | 2500ms | 4/1497 |
| ✅ | `catfact_random` | 99.8% | 99.4% | 255.5 | 10080.2 | 3000ms | 9/1497 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 96.8 | 4328.4 | 1500ms | 1/1497 |
| ✅ | `agify_name` | 99.93% | 99.73% | 384.7 | 16112.2 | 2000ms | 4/1497 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 205.4 | 3882.8 | 2000ms | 2/1497 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4339.2 | 75.0% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 3891.8 | 50.79% |
| `nasa_apod` | 17:00 | 3889.4 | 53.25% |
| `nasa_apod` | 01:00 | 3614.7 | 52.17% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 11:00 | 3496.8 | 51.19% |
| `nasa_apod` | 12:00 | 3477.2 | 53.03% |
| `nasa_apod` | 18:00 | 3445.4 | 48.75% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
